package handler 

import (
  "fmt"
  "log"
  "net/http"
  "os"

  "github.com/SmokierLemur51/gutterboy/middleware"

  "github.com/joho/godotenv"

  _ "github.com/mattn/go-sqlite3"
  "github.com/jmoiron/sqlx"
)



type CoreHandler struct {
  Port string
  DB   *sqlx.DB
}



func NewCoreHandler() *CoreHandler {
  return &CoreHandler{
    Port: ":5000",
  }
}




func (h *CoreHandler) Run() error {
  // Load .env
  err := godotenv.Load()
  if err != nil {
    return err
  }
  
  h.DB, err = sqlx.Connect("sqlite3", 
    fmt.Sprintf("instance/%s.db", os.Getenv("DB_FILE")))

  if err != nil {
    return err
  }
  
  router := http.NewServeMux()
  h.LoadRoutes(router)
  
  stack := middleware.CreateStack(
    middleware.Logging,
  )

  server := http.Server{
    Addr: h.Port, 
    Handler: stack(router),
  }
  
  log.Println("Starting server on port " + h.Port)
  return server.ListenAndServe()
}


