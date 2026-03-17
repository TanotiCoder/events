# Copyright (c) 2026, Tanoti and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventBooking(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from events.ticketing.doctype.event_booking_attendee.event_booking_attendee import EventBookingAttendee
        from frappe.types import DF

        amended_from: DF.Link | None
        attendee: DF.Table[EventBookingAttendee]
        currancy: DF.Link | None
        event: DF.Link
        total_amount: DF.Currency
        user: DF.Link | None
    # end: auto-generated types
    pass

    def validate(self):
        self.set_total()
        self.set_currency()

    def set_total(self):
        total = 0
        for attendee in self.attendee:
            total += attendee.amount
        self.total_amount = total

    def set_currency(self):
        if self.attendee and self.attendee[0].currency:
            self.currancy = self.attendee[0].currency
    
    def on_submit(self):
        self.generate_tickets()
    
    def generate_tickets(self):
        for attendee in self.attendee:
            ticket = frappe.new_doc("Event Ticket")
            ticket.event = self.event
            ticket.booking = self.name
            ticket.attendee_name = attendee.full_name
            ticket.ticket_type = attendee.ticket_type
            ticket.insert()
    