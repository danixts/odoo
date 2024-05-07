/** @odoo-module **/

import {PartnerDetailsEdit} from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import {ErrorPopup} from "@point_of_sale/app/errors/popups/error_popup";
import {patch} from "@web/core/utils/patch";

patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup()
        debugger;
        console.log({partner: this.pos.guru_module_data.find(e => e.id === 3)})
        this.changes.pin_code = this.props.partner.pin_code
        console.log("RENDER EDIT LIST COMPONENT")
    }
})