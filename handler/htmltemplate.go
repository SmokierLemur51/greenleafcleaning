package handler

import (
  "fmt"
  "html/template"
  "net/http"
)


type HtmlTemplate struct {
    Page         string
    CompanyName  string
    Title        string
    Content      map[string]interface{}
}

func (t HtmlTemplate) RenderTemplate(w http.ResponseWriter) error {
    tmpl, err := template.ParseFiles(fmt.Sprintf("templates/%s", t.Page))
    if err != nil {
        return err
    }
    err = tmpl.Execute(w, t)
    if err != nil {
        return err
    }
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    return nil
}
