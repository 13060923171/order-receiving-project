# -*- coding: utf-8 -*-
from pdf2docx import Converter

pdf_file = './PDF/Spark高级数据分析.pdf'
docx_file = './word/Spark高级数据分析.docx'
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

