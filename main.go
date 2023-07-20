package main

import (
	"github.com/SmokierLemur51/greenleafcleaning/routes"
	"github.com/gin-gonic/gin"
)

func main(){
	r := gin.Default()
	r.LoadHTMLGlob("templates/*")

	r.GET("/", routes.IndexHandler)

	r.Static("/static", "./static") // remember that the order to load static is important ... 
	r.Run(":5000")
}


