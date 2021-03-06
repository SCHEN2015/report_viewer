from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import (ModelView, CompactCRUDMixin,
                                    MasterDetailView)
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget
from flask_appbuilder import MultipleView

from . import appbuilder, db

from .models import (EC2_Report, AliyunReport, AzureReport, Bugs, FailureType,
                     FailureStatus, TestCases, EC2ReportCase, EC2Case)

# Below import is for charts
import calendar
from flask_appbuilder.charts.views import (DirectByChartView, DirectChartView,
                                           GroupByChartView)
from flask_appbuilder.models.group import (aggregate_sum, aggregate_count,
                                           aggregate, aggregate_avg)


class EC2_ReportPubView(ModelView):
    datamodel = SQLAInterface(EC2_Report)
    base_permissions = ["can_list", "can_show", "menu_access"]
    # list_widget = ListBlock
    # show_widget = ShowBlockWidget

    label_columns = {"result_url": "Result"}

    list_columns = [
        "log_id", "instance_type", "instance_available_date", "compose_id",
        "pkg_ver", "bug_id", "branch_name", "cases_pass", "cases_fail",
        "cases_cancel", "cases_other", "cases_total", "pass_rate", "test_date","testrun"
    ]
    search_columns = [
        "log_id", "ami_id", "instance_type", "instance_available_date",
        "compose_id", "pkg_ver", "bug_id", "branch_name", "cases_pass",
        "cases_fail", "cases_cancel", "cases_other", "cases_total",
        "pass_rate", "test_date", "comments", "platform","testrun"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "log_id", "ami_id", "instance_type", "instance_available_date",
                "compose_id", "pkg_ver", "bug_id", "result_url", "branch_name",
                "cases_pass", "cases_fail", "cases_cancel", "cases_other",
                "cases_total", "pass_rate", "test_date", "comments", "platform","testrun"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    # base_order = ("log_id", "asc")
    base_order = ("log_id", "desc")
    # base_filters = [["created_by", FilterEqualFunction, get_user]]


class EC2_ReportView(EC2_ReportPubView):
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit",
        "can_delete"
    ]

class EC2CasePubView(ModelView):
    datamodel = SQLAInterface(EC2ReportCase)
    base_permissions = ["can_list", "can_show", "menu_access"]
    #label_columns = {"failure_url": ""}

    list_columns = [
        "log_id", "instance_type", "compose_id",
        "pkg_ver", "branch_name", "testrun", "case_name","run_time",
        "case_result", "test_date","comments", "failure", "case_intro"
    ]
    search_columns = [
        "log_id", "instance_type", "compose_id",
        "pkg_ver", "branch_name", "testrun", "case_name","run_time",
        "case_result", "case_debuglog", "test_date","comments", "failure_id"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "log_id", "instance_type", "compose_id",
        "pkg_ver", "branch_name", "testrun", "case_name","run_time",
        "case_result", "case_debuglog", "test_date","comments", "failure", "case_intro"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    # base_order = ("log_id", "asc")
    base_order = ("log_id", "desc")
    # base_filters = [["created_by", FilterEqualFunction, get_user]]
class EC2CaseView(EC2CasePubView):
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit",
        "can_delete"
    ]

class EC2CaseSourcePubView(ModelView):
    datamodel = SQLAInterface(EC2Case)
    base_permissions = ["can_list", "can_show", "menu_access"]
    #label_columns = {"failure_url": ""}

    list_columns = [
        "case_id", "case_name", "bugzilla_id", "polarion_id",
        "component", "priority", "maintainer", "description","key_steps",
        "expected_result", "source","comments"
    ]
    search_columns = [
        "case_id", "case_name", "bugzilla_id", "polarion_id",
        "component", "priority", "maintainer", "description","key_steps",
        "expected_result", "source_url","comments"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "case_id", "case_name", "bugzilla_id", "polarion_id",
        "component", "priority", "maintainer", "description","key_steps",
        "expected_result", "source","comments"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    base_order = ("case_id", "desc")

class EC2CaseSourceView(EC2CaseSourcePubView):
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit",
        "can_delete"
    ]

class AliyunReportPubView(ModelView):
    datamodel = SQLAInterface(AliyunReport)
    base_permissions = ["can_list", "can_show", "menu_access"]

    label_columns = {"result_url": "Result"}

    list_columns = [
        "log_id", "instance_type", "instance_available_date", "compose_id",
        "pkg_ver", "bug_id", "branch_name", "cases_pass", "cases_fail",
        "cases_cancel", "cases_other", "cases_total", "pass_rate", "test_date"
    ]
    search_columns = [
        "log_id", "ami_id", "instance_type", "instance_available_date",
        "compose_id", "pkg_ver", "bug_id", "branch_name", "cases_pass",
        "cases_fail", "cases_cancel", "cases_other", "cases_total",
        "pass_rate", "test_date", "comments", "platform"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "log_id", "ami_id", "instance_type", "instance_available_date",
                "compose_id", "pkg_ver", "bug_id", "result_url", "branch_name",
                "cases_pass", "cases_fail", "cases_cancel", "cases_other",
                "cases_total", "pass_rate", "test_date", "comments", "platform"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    base_order = ("log_id", "desc")


class AliyunReportView(ModelView):
    datamodel = SQLAInterface(AliyunReport)
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit",
        "can_delete"
    ]
    label_columns = {"result_url": "Result"}
    list_columns = [
        "log_id", "instance_type", "instance_available_date", "compose_id",
        "pkg_ver", "bug_id", "branch_name", "cases_pass", "cases_fail",
        "cases_cancel", "cases_other", "cases_total", "pass_rate", "test_date",
        "comments"
    ]
    search_columns = [
        "log_id", "ami_id", "instance_type", "instance_available_date",
        "compose_id", "pkg_ver", "bug_id", "branch_name", "cases_pass",
        "cases_fail", "cases_cancel", "cases_other", "cases_total",
        "pass_rate", "test_date", "comments", "platform"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "log_id", "ami_id", "instance_type", "instance_available_date",
                "compose_id", "pkg_ver", "bug_id", "result_url", "branch_name",
                "cases_pass", "cases_fail", "cases_cancel", "cases_other",
                "cases_total", "pass_rate", "test_date", "comments", "platform"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    base_order = ("log_id", "desc")


class BugsPubView(ModelView):
    datamodel = SQLAInterface(Bugs)
    base_permissions = ["can_list", "can_show", "menu_access"]

    # label_columns = {"bug_url": "BZ#"}

    list_columns = [
        "id", "test_suite", "case_name", "bug_url", "bug_title",
        "failure_status", "failure_type", "comments", "last_update",
        "create_date"
    ]
    search_columns = [
        "id", "test_suite", "case_name", "bug_id", "bug_title",
        "failure_status", "branch_name", "comments", "last_update",
        "create_date", 'failure_type', 'identify_keywords',
        'identify_debuglog', 'contactor'
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "id", "test_suite", "case_name", "bug_id", "bug_title",
                "failure_status", "branch_name", "comments", "last_update",
                "create_date", 'failure_type', 'identify_keywords',
                'identify_debuglog', 'contactor'
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    # base_order = ("log_id", "asc")
    base_order = ("id", "desc")


class BugsView(BugsPubView):
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit",
        "can_delete"
    ]


class FailureTypeView(ModelView):
    datamodel = SQLAInterface(FailureType)
    related_views = [BugsView]


class FailureStatusView(ModelView):
    datamodel = SQLAInterface(FailureStatus)
    related_views = [BugsView]


def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


class EC2_TestRunChartView(DirectByChartView):
    datamodel = SQLAInterface(EC2_Report)
    chart_title = "EC2 Test Per Run"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "EC2 Pass Rate",
            "group": "test_date",
            "series": ["pass_rate"],
        },
        {
            "label":
            "EC2 Test Per Run",
            "group":
            "test_date",
            "series": [
                "cases_total",
                "cases_pass",
                "cases_fail",
                "cases_cancel",
                "cases_other",
            ],
        },
        #        {
        #            "group": "month_year",
        #            "formatter": pretty_month_year,
        #            "series": [
        #                (aggregate_sum, "cases_total"),
        #                (aggregate_sum, "cases_fail"),
        #            ],
        #        },
    ]


class AliyunTestRunChartView(DirectByChartView):
    datamodel = SQLAInterface(AliyunReport)
    chart_title = "Aliyun Test Per Run"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "Aliyun Pass Rate",
            "group": "test_date",
            "series": ["pass_rate"],
        },
        {
            "label":
            "Aliyun Test Per Run",
            "group":
            "test_date",
            "series": [
                "cases_total",
                "cases_pass",
                "cases_fail",
                "cases_cancel",
                "cases_other",
            ],
        },
    ]


# @aggregate(label='Total diff')
# def aggregate_total(items, col):
#    """
#        Function to count how many diff itmes found.
#        accepts a list and returns the sum of the list's items
#    """
#    col_list = []
#    col_list.append(getattr(item, col) for item in items)
#    #col_set = set(col_list)
#    #print("%s"%items)
#    return len(items)


class EC2_TestSumChartView(GroupByChartView):
    datamodel = SQLAInterface(EC2_Report)
    chart_title = "EC2 Test Sum"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "EC2 Test By Day",
            "group": "test_date",
            "series": [
                (aggregate_sum, "cases_total"),
            ],
        },
        {
            "label": "EC2 Test By Instance",
            "group": "instance_type",
            "series": [
                (aggregate_count, "instance_type"),
            ],
        },
        {
            "label": "EC2 Test By Compose ID",
            "group": "compose_id",
            "series": [
                (aggregate_count, "compose_id"),
            ],
        },
    ]


class AliyunTestSumChartView(GroupByChartView):
    datamodel = SQLAInterface(AliyunReport)
    chart_title = "Aliyun Test Sum"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "Aliyun Test By Day",
            "group": "test_date",
            "series": [
                (aggregate_sum, "cases_total"),
            ],
        },
        {
            "label": "Aliyun Test By Instance",
            "group": "instance_type",
            "series": [
                (aggregate_count, "instance_type"),
            ],
        },
        {
            "label": "Aliyun Test By Compose ID",
            "group": "compose_id",
            "series": [
                (aggregate_count, "compose_id"),
            ],
        },
    ]


class TestBugsByCaseChartView(GroupByChartView):
    datamodel = SQLAInterface(Bugs)
    chart_title = "Test Bugs by Case"
    chart_type = 'ColumnChart'

    definitions = [
        {
            "label": "Test Bugs by Case",
            "group": "case_name",
            "series": [
                (aggregate_count, "case_name"),
            ],
        },
    ]


class TestCasesView(ModelView):
    datamodel = SQLAInterface(TestCases)
    base_permissions = [
        "can_list", "can_show", "menu_access", "can_add", "can_edit"
    ]
    list_columns = [
        "case_id", "case_title", "ec2_casename", "azure_casename",
        "aliyun_casename", "openstack_casename", "esx_casename",
        "hyperv_casename", "create_date","create_by"
    ]
    search_columns = [
        "case_id", "case_title", "case_description", "case_keycmd", "ec2_repo",
        "ec2_casename", "ec2_owner", "ec2_comments", "azure_repo",
        "azure_casename", "azure_owner", "azure_comments", "aliyun_repo",
        "aliyun_casename", "aliyun_owner", "aliyun_comments",
        "openstack_repo","openstack_casename","openstack_owner","openstack_comments",
        "esx_repo","esx_casename", "esx_owner", "esx_comments", "hyperv_repo",
        "hyperv_casename", "hyperv_owner", "hyperv_comments", "create_date",
        "last_update", "create_by", "comments"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "case_id", "case_title", "case_description", "case_keycmd",
                "ec2_repo", "ec2_casename", "ec2_owner", "ec2_comments",
                "azure_repo", "azure_casename", "azure_owner",
                "azure_comments", "aliyun_repo", "aliyun_casename",
                "aliyun_owner", "aliyun_comments",
                "openstack_repo","openstack_casename","openstack_owner",
                "openstack_comments", "esx_repo", "esx_casename",
                "esx_owner", "esx_comments", "hyperv_repo", "hyperv_casename",
                "hyperv_owner", "hyperv_comments", "create_date",
                "last_update", "create_by", "comments"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    base_order = ("case_id", "desc")


class AzureReportView(ModelView):
    datamodel = SQLAInterface(AzureReport)
    base_permissions = ["can_list", "can_show", "menu_access"]
    label_columns = {"log": "Result"}
    list_columns = [
        "rhel", "version", "vm_size", "result", "tests", "failures", "errors",
        "skipped", "finished_time", "log_link"
    ]
    search_columns = [
        "rhel", "version", "vm_size", "automation_tool", "result", "tests",
        "failures", "errors", "skipped", "finished_time"
    ]

    show_fieldsets = [
        ("Summary", {
            "fields": [
                "rhel", "version", "vm_size", "automation_tool", "result",
                "tests", "failures", "errors", "skipped", "failed_cases",
                "rerun_failed_cases", "duration", "finished_time", "log_link"
            ]
        }),
        ("Description", {
            "fields": ["description"],
            "expanded": True
        }),
    ]
    base_order = ("finished_time", "desc")


db.create_all()
appbuilder.add_view(EC2_ReportPubView,
                    "EC2 Test Reports",
                    icon="fa-folder-open-o",
                    category="TestReports")
appbuilder.add_view(EC2_ReportView,
                    "Edit EC2 Test Reports",
                    icon="fa-envelope",
                    category="Management")
appbuilder.add_view(EC2CasePubView,
                    "EC2 Test Reports by Cases",
                    icon="fa-folder-open-o",
                    category="TestReports")
appbuilder.add_view(EC2CaseView,
                    "Edit EC2 Test Reports by Cases",
                    icon="fa-envelope",
                    category="Management")

appbuilder.add_view(AliyunReportPubView,
                    "Aliyun Test Reports",
                    icon="fa-folder-open-o",
                    category="TestReports")
appbuilder.add_view(AliyunReportView,
                    "Edit Aliyun Test Reports",
                    icon="fa-envelope",
                    category="Management")

appbuilder.add_view(AzureReportView,
                    "Azure Test Reports",
                    icon="fa-folder-open-o",
                    category="TestReports")

appbuilder.add_view(BugsPubView,
                    "List Know Failures",
                    icon="fa-folder-open-o",
                    category="TestBugs")
appbuilder.add_view(BugsView,
                    "Edit Know Failures",
                    icon="fa-envelope",
                    category="Management")
appbuilder.add_view(FailureTypeView,
                    "Edit Know Failures Types",
                    icon="fa-envelope",
                    category="Management")
appbuilder.add_view(FailureStatusView,
                    "Edit Failures Status List",
                    icon="fa-envelope",
                    category="Management")
appbuilder.add_separator("Management")

appbuilder.add_view(EC2_TestRunChartView,
                    "EC2 Test Per Run",
                    icon="fa-folder-open-o",
                    category="DataAnalyze")
appbuilder.add_view(EC2_TestSumChartView,
                    "EC2 Test Sum",
                    icon="fa-folder-open-o",
                    category="DataAnalyze")

appbuilder.add_view(AliyunTestRunChartView,
                    "Aliyun Test Per Run",
                    icon="fa-folder-open-o",
                    category="DataAnalyze")
appbuilder.add_view(AliyunTestSumChartView,
                    "Aliyun Test Sum",
                    icon="fa-folder-open-o",
                    category="DataAnalyze")

appbuilder.add_view(TestBugsByCaseChartView,
                    "Test Bugs by Case",
                    icon="fa-folder-open-o",
                    category="DataAnalyze")

appbuilder.add_view(EC2CaseSourcePubView,
                    "EC2 Test Cases Source",
                    icon="fa-folder-open-o",
                    category="TestCases")
appbuilder.add_view(EC2CaseSourceView,
                    "Edit EC2 Test Cases",
                    icon="fa-envelope",
                    category="Management")
appbuilder.add_view(TestCasesView(), "GernalCasesTrack")

# appbuilder.add_separator("TestReports")
# appbuilder.add_separator("Management")
