package handler

import ( 
  "net/http"
)

// Load all sales routes
func (h *CoreHandler) LoadRoutes(router *http.ServeMux) *http.ServeMux {
  router.HandleFunc("GET /", h.IndexHandler)
  
  return router
}



func (h *CoreHandler) IndexHandler(w http.ResponseWriter, r *http.Request) {
  index := HtmlTemplate{Page: "index.html"}
  index.RenderTemplate(w)
}



func (h *CoreHandler) NewOrderHandler(w http.ResponseWriter, r *http.Request) {
  // Create new session for database 

  p := HtmlTemplate()
  p.RenderTemplate(w)
}


func (h *CoreHandler) AddToOrder(w http.ResponseWriter, r *http.Request) {
  p := HtmlTemplate()
  p.RenderTemplate(w)
}
