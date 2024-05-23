package handler

import (
	"net/http"
)

// Load all sales routes
func (h *CoreHandler) LoadRoutes(router *http.ServeMux) *http.ServeMux {
	// Html page get requests
	router.HandleFunc("GET /", h.IndexPageHandler)
	router.HandleFunc("GET /contact", h.ContactPagehandler)

	// Post requests
	router.HandleFunc("POST /contact", h.ProcessContactFormHandler)

	return router
}

func (h *CoreHandler) IndexPageHandler(w http.ResponseWriter, r *http.Request) {
	// Render index page
	index := HtmlTemplate{Page: "index.html", Title: "Logan Lee"}
	index.RenderTemplate(w)
}

func (h *CoreHandler) ContactPagehandler(w http.ResponseWriter, r *http.Request) {
	// Render contact page
	contact := HtmlTemplate{
		Page:  "contact.html",
		Title: "Contact Us",
	}
	contact.RenderTemplate(w)
}

func (h *CoreHandler) ProcessContactFormHandler(w http.ResponseWriter, r *http.Request) {
	// Process the contact form for errors

}

func (h *CoreHandler) NewOrderHandler(w http.ResponseWriter, r *http.Request) {
	// Create new session for database

	p := HtmlTemplate{}
	p.RenderTemplate(w)
}

func (h *CoreHandler) AddToOrder(w http.ResponseWriter, r *http.Request) {
	p := HtmlTemplate{}
	p.RenderTemplate(w)
}
