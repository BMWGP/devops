""
========================
Author：Jerry
Time：2022/3/25
Project：day14
Company：上海零檬信息技术有限公司
========================
""
#使用pytest收樂所有的用例并运行，输出allure报告
import pytest
import os

from common.my_path import report_dir
pytest.main(["--alluredir=reports",“--junitxml=result.xml"])