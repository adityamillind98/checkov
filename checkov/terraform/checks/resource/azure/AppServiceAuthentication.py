from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class AppServiceAuthentication(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure App Service Authentication is set on Azure App Service"
        id = "CKV_AZURE_13"
        supported_resources = ('azurerm_app_service', 'azurerm_linux_web_app', 'azurerm_windows_web_app')
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_block_result=CheckResult.FAILED)

    def get_inspected_key(self):
        return 'auth_settings/[0]/enabled/[0]'


check = AppServiceAuthentication()
