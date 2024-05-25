package handler

import (
	"net/http"

	"github.com/go-chi/chi/v5"
)

// Load all sales routes
func (h *CoreHandler) LoadRoutes() {
	h.Router.Group(func(chi.Router) {
		// GET requests
		h.Router.Method(http.MethodGet, "/", h.IndexPageHandler())
		h.Router.Method(http.MethodGet, "/contact", h.ContactPagehandler())
	})
}

func (h *CoreHandler) IndexPageHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// Render index page
		index := HtmlTemplate{Page: "index.html"}
		index.RenderTemplate(w)
	}
}

func (h *CoreHandler) ContactPagehandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// Render contact page
		contact := HtmlTemplate{
			Page:  "contact.html",
			Title: "Contact Us",
		}
		contact.RenderTemplate(w)
	}
}

/*
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
*/
