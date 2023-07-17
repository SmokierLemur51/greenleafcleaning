package routes

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func IndexHandler(c *gin.Context){
	c.HTML(http.StatusOK, "index.html", gin.H{
		"title": "Greenleaf Cleaning",
	})
}