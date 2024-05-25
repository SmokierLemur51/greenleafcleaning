package handler

import (
	"fmt"
	"log"
	"net/http"
	"os"

	// Internal packages
	// "github.com/SmokierLemur51/gutterboy/middleware"

	"github.com/go-chi/chi/v5"
	"github.com/jmoiron/sqlx"
	"github.com/joho/godotenv"
	_ "github.com/mattn/go-sqlite3"
)

type CoreHandler struct {
	Port   string
	Router *chi.Mux
	DB     *sqlx.DB
}

func NewCoreHandler() *CoreHandler {
	h := &CoreHandler{}
	h.Port = ":5000"
	h.Router = chi.NewRouter()
	return h
}

func (h *CoreHandler) Run() error {
	// Load .env
	err := godotenv.Load()
	if err != nil {
		return err
	}
	// Database connection
	h.DB, err = sqlx.Connect("sqlite3",
		fmt.Sprintf("instance/%s.db", os.Getenv("DB_FILE")))

	if err != nil {
		return err
	}

	h.Router.Handle(
		"/static/*", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))
	h.LoadRoutes()

	log.Println("Starting server on port " + h.Port)
	return http.ListenAndServe(h.Port, h.Router)
}
