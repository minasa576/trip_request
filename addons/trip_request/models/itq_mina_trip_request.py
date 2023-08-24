from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    allowed_destinations = fields.Many2many('res.country', string="Allowed Destinations")
    trip_request_ids = fields.One2many('itq.trip.request', 'employee_id', string="Trip Requests")


class ItqTripRequest(models.Model):
    _name = "itq.trip.request"

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, domain="[('contract_id.state', '=', 'open')]")
    destination_id = fields.Many2one('res.country', string="Destination", required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    number_of_rest_days = fields.Integer(required=True)
    trip_days = fields.Integer(string="Trip Days", compute="calc_trip_days")
    state = fields.Selection(
        [('draft', "Draft"), ('confirmed', "Confirmed"), ('ended', "Ended"), ('cancelled', "Cancelled")])
    last_state_change_by_id = fields.Many2one('res.users', string="Last Status Change By", readonly=True)
    allowed_destinations_ids = fields.Many2many(related="employee_id.allowed_destinations")

    @api.onchange('start_date')
    def set_end_date_to_empty(self):
        self.end_date = False

    @api.depends('start_date', 'end_date', 'number_of_rest_days')
    def calc_trip_days(self):
        for rec in self:
            if rec.end_date and rec.start_date and rec.end_date >= rec.start_date:
                rec.trip_days = (rec.end_date - rec.start_date).days - rec.number_of_rest_days
                if rec.trip_days < 0:
                    rec.trip_days = 0
            else:
                rec.trip_days = 0

    def write(self, values):
        print(values)
        if 'state' in values:
            values['last_state_change_by_id'] = self.env.user
        return super(ItqTripRequest, self).write(values)
