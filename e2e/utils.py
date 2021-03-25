from . import KIBANA_URL


def log_in(user, page):
    # go to kibana
    page.goto(KIBANA_URL)
    # accept the monitoring notice
    page.click(".island-button.js-notice-submit")
    # select the cloud.gov IdP
    page.click("a>span:has-text('cloud.gov')")
    page.fill("input[id='username']", user.username)
    page.fill("input[id='password']", user.password)
    page.click("text='Login'")
    page.fill("input[id='j_tokenNumber']", user.totp.now())
    page.click("text='Login'")
    # lots of redirects and stuff happen here, so just, like, chill, ok?
    page.wait_for_load_state("networkidle")
    if "/authorize?" in page.url:
        # first time using this app with this user
        page.click("text='Authorize'")


def switch_tenants(page, tenant="Global"):
    """
    switch to the specified tenant.
    Must start on a page with the user menu accessible.
    """
    # open the user menu
    page.click("id=actionsMenu")
    page.wait_for_load_state("networkidle")
    # open the switch tenant pane
    page.click("text=Switch tenants")
    page.wait_for_load_state("networkidle")
    # select the global tenant
    page.click(f"text={tenant}")
    page.wait_for_load_state("networkidle")
    # submit
    page.click("text=Confirm")
    page.wait_for_load_state("networkidle")

    # this page takes a few seconds, but playwright doesn't seem to think anything is happening
    # todo: find a better thing to wait for here.
    page.wait_for_timeout(2000)
