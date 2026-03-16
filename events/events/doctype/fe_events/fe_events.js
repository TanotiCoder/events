// Copyright (c) 2026, Tanoti and contributors
// For license information, please see license.txt

frappe.ui.form.on("FE Events", {
    onload(frm) {
        // Use 'onload' instead of 'refresh' to fetch this only once when the form loads.
        // 'refresh' triggers every time you save, submit, or reload the doc, 
        // which causes unnecessary network traffic.
        
        frappe.call({
            method: "frappe.geo.country_info.get_country_timezone_info",
            callback: (r) => {
                if (r.message && r.message.all_timezones) {
                    // Update the options
                    frm.set_df_property("time_zone", "options", r.message.all_timezones);
                    
                    // Optional: If the field is currently empty, set a default
                    if (!frm.doc.time_zone && frappe.sys_defaults.time_zone) {
                        frm.set_value("time_zone", frappe.sys_defaults.time_zone);
                    }
                }
            }
        });
    }
});