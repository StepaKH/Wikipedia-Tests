from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base.base_page import BasePage

class SavedButtons(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Protected Locators
    POSITIVE_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/positiveButton']")
    NEGATIVE_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/negativeButton']")
    EMPTY_TITLE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/empty_title']")
    MESSAGE_TITLE_VIEW_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/messageTitleView']")
    CONTAINER_CLICK_AREA = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='org.wikipedia.alpha:id/containerClickArea']")
    FILTER_MY_LISTS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Filter my lists']")
    MORE_OPTIONS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='More options']")
    SELECT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_select']")
    SORT_BY_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_sort_by']")
    CREATE_NEW_LIST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_create_new_list']")
    IMPORT_LIST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_import_list']")
    REFRESH_SYNC_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Refresh sync']")
    CHECK_ALL_ITEMS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Check all items']")
    DONE_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Done']")
    SORT_OPTIONS_LIST_RV = (AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='org.wikipedia.alpha:id/sort_options_list']")
    CANCEL_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    BROWSE_FILES_IN_OTHER_APPS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='BROWSE FILES IN OTHER APPS']")
    CREATE_AN_ACCOUNT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Create an account']")
    NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    SAVED_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']")

    CONTINUE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    GET_STARTED_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
