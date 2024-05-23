package data

import (
	"database/sql"
	"time"
)

/*
	For all contact related data.
		- Contact Requests
		- Contact Information
		- Conversations with Contact Requests
*/

type ContactRequest struct {
	ID        int            `db:"id"`
	CreatedAt time.Time      `db:"created_at"`
	UpdatedAt time.Time      `db:"updated_at"`
	DeletedAt sql.NullTime   `db:"deleted_at"`
	Contacted bool           `db:"completed"`
	Name      string         `db:"name"`
	Phone     string         `db:"phone"`
	Email     sql.NullString `db:"email"`
	Messaage  sql.NullString `db:"message"`
}

// This guy is going to be what I learned when reaching out
// to customers.
type ContactRequestNote struct{}

type Contact struct{}
