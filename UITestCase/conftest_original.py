# Author: Yi Sun(Tim) 2025-06-16

import pytest
import os
from pathlib import Path
from selenium import webdriver
from CommonModule.read_config import ReadConfig

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 先执行默认行为
    outcome = yield
    report = outcome.get_result()

    # 仅在测试执行失败时处理
    if report.when == "call" and report.failed:
        # 获取测试文件所在目录（绝对路径）
        test_dir = Path(item.fspath).parent.absolute()
        screenshot_dir = test_dir / "screenshots"

        # 打印调试信息（实际使用时可以移除）
        print(f"\n[DEBUG] 测试文件路径: {item.fspath}")
        print(f"[DEBUG] 截图目录: {screenshot_dir}")

        # 确保目录存在
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        # 获取driver实例
        driver = item.funcargs.get('driver')
        if driver:
            try:
                screenshot_path = screenshot_dir / f"{item.name}.png"
                driver.save_screenshot(str(screenshot_path))
                print(f"[SUCCESS] 截图已保存到: {screenshot_path}")
            except Exception as e:
                print(f"[ERROR] 截图失败: {str(e)}")
        else:
            print("[WARNING] 未找到driver实例")

    # # 获取测试文件所在目录的绝对路径
    # test_file_dir = Path(item.location[0]).parent.absolute() # item.location[0] 是测试文件的绝对路径
    # screenshot_dir = test_file_dir / "screenshots"
    # print(f"截图目录路径: {screenshot_dir}")  # 调试语句
    #
    # # 强制创建目录（即使多级目录不存在）
    # os.makedirs(screenshot_dir, exist_ok=True)  # 关键修改：用 os.makedirs 替代 Path.mkdir
    #
    # # 失败截图
    # if rep.when == "call" and rep.failed:
    #     print("测试失败，尝试截图...")  # 调试语句
    #     driver = item.funcargs.get("driver")
    #     print(f"获取到的 driver: {driver}")  # 调试语句
    #     if driver and hasattr(driver, "save_screenshot"):
    #         screenshot_path = screenshot_dir / f"{item.name}.png"
    #         try:
    #             driver.save_screenshot(str(screenshot_path))
    #             print(f"\n✅ 截图已保存到: {screenshot_path}")  # 明确成功提示
    #         except Exception as e:
    #             print(f"\n❌ 截图失败: {str(e)}")


@pytest.fixture(scope="class")
def credentials():
    config_read = ReadConfig()
    return {
        "egd_url":config_read.get_url(),
        "admin_username": config_read.admin_username(),
        "admin_password": config_read.admin_password()
    }

# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def driver(credentials):                         # 依赖credentials fixture
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(credentials["egd_url"])
    yield driver
    driver.quit()