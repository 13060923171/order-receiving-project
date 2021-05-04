import json, requests, time, datetime

class get_zabbix_alert():
    def __init__(self, zabbix_user, zabbix_passwd, zabbix_api_url):
        self.zabbix_user = zabbix_user
        self.zabbix_passwd = zabbix_passwd
        self.zabbix_api_url = zabbix_api_url
        self.zabbix_request_header = {"Content-Type": "application/json"}
        self.get_zabbix_authcode()

    # 获取认证信息
    def get_zabbix_authcode(self):
        params = json.dumps({
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.zabbix_user,
                "password": self.zabbix_passwd
            },
            "id": 1,
        })
        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        auth = res["result"]
        self.zabbix_authcode = auth
        pass

    # 获取时间区间
    def get_time_str(self, day):
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        ts = int(time.mktime(time.strptime(dt, '%Y-%m-%d')))
        if day <= 0:
            return time.time(), ts - 86400 * 3650
        return ts, ts - 86400 * day

    # 获取所有告警列表
    def get_all_alert_list(self, time_start, time_stop):
        params = json.dumps({
            "jsonrpc": "2.0",
            "method": "alert.get",
            "params": {
                "output": ["eventid"],
                "selectHosts": ["hostid"],
                "time_from": time_start,
                "time_till": time_stop
            },
            "auth": self.zabbix_authcode,
            "id": 1
        })

        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        alert_host_list = []
        for host in list(res["result"]):
            alert_host_list.append(host["eventid"])
        return alert_host_list

    # 获取告警时间的信息
    def get_event_info(self, id):
        params = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "event.get",
                "params": {
                    "output": ["severity"],
                    "eventids": id,
                    "selectHosts": ["name"]
                },
                "auth": self.zabbix_authcode,
                "id": 1
            }
        )
        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        event_list = []
        for data in res["result"]:
            obj = {
                "level": data["severity"],
                "hostname": data["hosts"][0]["name"],
                "hostid": data["hosts"][0]["hostid"],
                "eventid": data["eventid"]
            }
            event_list.append(obj)
        return event_list

    # 获取主机信息
    def get_host_info(self, id):
        params = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid"],
                "filter": {
                    "hostid": id
                },
                "selectGroups": ["name"]
            },
            "auth": self.zabbix_authcode,
            "id": 1
        })

        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        hostgroup_list = []
        for data in res["result"]:
            obj = {
                "hostid": data["hostid"],
                "groupname": data["groups"][0]["name"]
            }
            hostgroup_list.append(obj)
        return hostgroup_list

    # 通过事件ID查找事件信息
    def get_event_by_eventid(self, id):
        params = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "event.get",
                "params": {
                    "output": ["name"],
                    "eventids": id
                },
                "auth": self.zabbix_authcode,
                "id": 1
            }
        )

        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)

        return res["result"]

    # 生成html代码
    def get_table_html(self, day):
        timezone = self.get_time_str(day)
        evenid_list = self.get_all_alert_list(timezone[1], timezone[0])
        event_list = self.get_event_by_eventid(evenid_list)
        evenid_to_trigger = {}

        for data in event_list:
            evenid_to_trigger[data["eventid"]] = data["name"]

        event_info_list = self.get_event_info(evenid_list)
        event_info_list_copy = event_info_list.copy()
        for data in event_info_list_copy:
            if data["level"] == '0':
                event_info_list.remove(data)
        hostid_list = []
        for data in event_info_list:
            hostid_list.append(data["hostid"])
        hostid_groupname = self.get_host_info(hostid_list)
        hostid_to_groupname = {}
        for data in hostid_groupname:
            hostid_to_groupname[data["hostid"]] = data["groupname"]

        for num in range(len(event_info_list)):
            event_info_list[num]["groupname"] = hostid_to_groupname[event_info_list[num]["hostid"]]
            event_info_list[num]["eventname"] = evenid_to_trigger[event_info_list[num]["eventid"]]

        trigger_rank = {}
        group_rank = {}
        trigger_description_obj = self.make_trigger_description_obj(evenid_list)
        item_description_obj = self.make_item_description_obj(evenid_list)

        for data in event_info_list:
            if data["groupname"] in group_rank:
                group_rank[data["groupname"]] += 1
            else:
                group_rank[data["groupname"]] = 1
            try:
              event_str = data["eventname"] + '~~~' + data["hostname"] + '~~~' + data["level"] + '~~~' + data[
                  "groupname"]  + '~~~' + trigger_description_obj[data["eventname"]] + '~~~' + item_description_obj[data["eventname"]]
            except:
              event_str = data["eventname"] + '~~~' + data["hostname"] + '~~~' + data["level"] + '~~~' + data[
                  "groupname"]  + '~~~' + trigger_description_obj[data["eventname"]] + '~~~' + ' '

            if event_str in trigger_rank:
              trigger_rank[event_str] += 1

            else:
              trigger_rank[event_str] = 1

        alert_rank_list = list(group_rank.items())
        html_str = ''
        for data in alert_rank_list:
            try:
                origin = data[0].split('_')[1].split('-')[0]
            except:
                origin = ''
            tail_html_str = '''<tr><td>{}</td><td class="m_td">{}</td><td class="m_td">{}</td></tr>'''.format(data[0],origin,data[1])
            html_str = html_str + tail_html_str

        trigger_rank_list = list(trigger_rank.items())
        trigger_html_str = ''
        name = ''
        trigger_conut_rank = []

        for i in trigger_rank_list:
            max = 0
            for data in trigger_rank_list:
                if data[0] in trigger_conut_rank:
                    continue
                if data[1] > max:
                    max = data[1]
                    name = data[0]
            trigger_conut_rank.append(name)

        for data in trigger_conut_rank:
            host_and_trigger = data.split('~~~')
            tail_html_str = '''<tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td class="m_td">{}</td>
            <td class="m_td">{}</td>
            <td class="m_td">{}</td>
            </tr>'''.format(
                host_and_trigger[1], trigger_rank[data], host_and_trigger[3], host_and_trigger[0], host_and_trigger[2], host_and_trigger[-2], host_and_trigger[-1])
            trigger_html_str = trigger_html_str + tail_html_str

        return html_str, trigger_html_str

    def get_trigger_by_eventid(self, id):
        params = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "event.get",
                "params": {
                    "output": ["name"],
                    "eventids": id,
                    "selectRelatedObject": ["comments"]
                },
                "auth": self.zabbix_authcode,
                "id": 1
            }
        )

        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        return res["result"]

    def get_item_by_triggerid(self, id):
        trigger_list = self.get_trigger_by_eventid(id)
        triggerids_list = []
        for data in trigger_list:
            triggerids_list.append(data["relatedObject"]["triggerid"])

        params = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "trigger.get",
                "params": {
                    "output": ["description"],
                    "triggerids": triggerids_list,
                    "selectItems": ["description"]
                },
                "auth": self.zabbix_authcode,
                "id": 1
            }
        )

        res = requests.post(url=self.zabbix_api_url, headers=self.zabbix_request_header, data=params)
        res = json.loads(res.text)
        return res["result"]

    def make_trigger_description_obj(self, evenids):
        trigger_list = self.get_trigger_by_eventid(evenids)
        eventid_trigger_des_obj = {}
        for data in trigger_list:
            eventid_trigger_des_obj[data["name"]] = data["relatedObject"]["comments"]
        return eventid_trigger_des_obj

    def make_item_description_obj(self, evenids):

        item_list = self.get_item_by_triggerid(evenids)
        triggerid_item_des_obj = {}
        for data in item_list:
            triggerid_item_des_obj[data["description"]] = ""
            for item_data in data["items"]:
                triggerid_item_des_obj[data["description"]] = triggerid_item_des_obj[data["description"]] + ' ' + item_data["description"]
        return  triggerid_item_des_obj

def get_time_str(day):
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    ts = int(time.mktime(time.strptime(dt, '%Y-%m-%d')))
    if day <= 0:
        return time.time(), ts - 86400 * 3650
    return ts, ts - 86400 * day



