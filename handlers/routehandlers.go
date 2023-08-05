package handlers

import (
	"net/http"
	"log"

	"github.com/SmokierLemur51/greenleafcleaning/models"
	"github.com/SmokierLemur51/greenleafcleaning/models"
	"github.com/SmokierLemur51/greenleafcleaning/utils"
)

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	page := models.PageData{
		Page: "index.html",
		Title: "Greenleaf Cleaning",
		Message: "Fucking hell its all gone, time to start over ... ",
	}

	err := utils.RenderTemplate(w, page.Page, page)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}