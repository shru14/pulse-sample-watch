terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "notes" {
  name     = "rg-call-notes"
  location = "westeurope"
}

resource "azurerm_postgresql_flexible_server" "notes" {
  name                = "psql-call-notes"
  resource_group_name = azurerm_resource_group.notes.name
  location            = azurerm_resource_group.notes.location
  sku_name            = "GP_Standard_D2s_v3"
  version             = "16"
}

resource "azurerm_search_service" "calls" {
  name                = "srch-call-notes"
  resource_group_name = azurerm_resource_group.notes.name
  location            = "westeurope"
  sku                 = "basic"
}
