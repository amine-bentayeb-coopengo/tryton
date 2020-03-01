# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import work
from . import timesheet
from . import invoice


def register():
    Pool.register(
        work.Work,
        work.WorkInvoicedProgress,
        timesheet.Line,
        invoice.InvoiceLine,
        module='project_invoice', type_='model')
    Pool.register(
        work.OpenInvoice,
        module='project_invoice', type_='wizard')
