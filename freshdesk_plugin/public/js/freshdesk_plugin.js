frappe.db.get_doc('Freshdesk Settings')
.then(function(r){
    console.log('Loaded Freshdesk Settings')

    function initFreshChat() {
        
        window.fcWidget.init({
            token: r.freshdesk_token,
            host: r.freshdesk_host,
            siteId: r.freshdesk_website_id
        });

        window.fcWidget.user.setFirstName(frappe.user_info().fullname);
        window.fcWidget.user.setEmail(frappe.user_info().email);
    }
    function initialize(i, t) { var e; i.getElementById(t) ? initFreshChat() : ((e = i.createElement("script")).id = t, e.async = !0, e.src = "https://wchat.eu.freshchat.com/js/widget.js", e.onload = initFreshChat, i.head.appendChild(e)) } function initiateCall() { initialize(document, "freshchat-js-sdk") } window.addEventListener ? window.addEventListener("load", initiateCall, !1) : window.attachEvent("load", initiateCall, !1);
})
