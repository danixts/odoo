/** @odoo-module **/
import {PosStore} from "@point_of_sale/app/store/pos_store";
import {PosDB} from "@point_of_sale/app/store/db";
import {patch} from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async _load_guru_data() {
        return await this.env.services.rpc('/web/dataset/call_kw/pos.session/get_data_guru', {
            model: 'pos.session',
            method: 'get_data_guru',
            args: [[]],
            kwargs: {}
        });
    },
    async _processData(loadedDate) {
        await super._processData(loadedDate);
        this.guru_module_data = await this._load_guru_data()
    }
})