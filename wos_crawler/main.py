from gui.main_gui import *
import settings
from scrapy import cmdline


def crawl_by_journal(journal_list_path, output_path='../output', document_type='Article', output_format='fieldtagged'):
    cmdline.execute(
        r'scrapy crawl wos_journal_spider -a journal_list_path={} -a output_path={} -a output_format={}'.format(
            journal_list_path, output_path, output_format).split() + ['-a', 'document_type={}'.format(
            document_type)])


def crawl_by_query(query, output_path='../output', document_type='Article', output_format='fieldtagged'):

    cmdline.execute(
        r'scrapy crawl wos_advanced_query_spider -a output_path={} -a output_format={}'.format(
            output_path, output_format).split() +
        ['-a', 'query={}'.format(query), '-a', 'document_type={}'.format(document_type)])


def crawl_by_gui():
    app = QApplication(sys.argv)
    gui_crawler = GuiCrawler()
    gui_crawler.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # 按期刊下载
    # crawl_by_journal(journal_list_path=r'C:\Users\Tom\PycharmProjects\wos_crawler\input\journal_list_test.txt',
    #                  output_path='../output', output_format='bibtex', document_type='letter')

    # 按检索式下载
    crawl_by_query(query='TS=information science AND PY=2018',
                   output_path='../output', output_format='bibtex', document_type='meeting abstract')

    # 使用GUI下载
    # crawl_by_gui()
    pass
