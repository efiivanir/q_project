"""Command Line Interface (CLI) for qinvest project."""

import click
import sys
from IPython import embed
from contextlib import contextmanager
import qinvest as qi
import pandas as _pd
from qinvest.Common import Common as co


# The main entry point for qinvest.
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.0')
def qinvest_cli():
    """Run the qinvest application."""


@qinvest_cli.command(help="open ipython shell with qinvest module")
def shell():
    embed()


@qinvest_cli.command(help="reports of stock")
@click.argument('ticker',default='SPY')
@click.option('--list', default=False, is_flag=True, help='get list of all reports types')
@click.option('--history', default=False, is_flag=True, help='report ticker history for 10y')
@click.option('--details',nargs=1,
              type=click.Choice(qi.Finance.get_yfinance_details_options()),
              help='report stock details'
              )
def reports(ticker,list,history,details):
    """ticker reports"""
    excel_file = ticker + '.xlsx'

    if list:
        print('\n'.join(qi.Finance.get_yfinance_details_options()))
    elif history:
        stock = qi.Finance.get_yfinace_history(ticker)
        writer = _pd.ExcelWriter(excel_file,
                                 datetime_format="YYYY-MM-DD",
                                 date_format="YYYY-MM-DD",
                                 )
        stock.to_excel(writer, sheet_name='history')
        writer.save()
        co.cleanExcel(excel_file)

    elif details:
        if details == 'all':
            writer = _pd.ExcelWriter(excel_file)
            all = qi.Finance.get_yfinance_stock_details_all(ticker)
            for d in all.keys():
                stock = all[d]
                stock.to_excel(writer, sheet_name=d)
            writer.save()
            co.cleanExcel(excel_file)
        else:
            writer = _pd.ExcelWriter(excel_file)
            stock = qi.Finance.get_yfinance_stock_details(ticker,details)
            stock.to_excel(writer, sheet_name=details)
            writer.save()
            co.cleanExcel(excel_file)

if __name__ == '__main__':
    qinvest_cli()
