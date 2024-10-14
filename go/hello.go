package main

import (
	"fmt"
	"time"
)

func greet(name string) string {
	return fmt.Sprintf("Hello, %s! Welcome to Go programming!", name)
}

func main() {
	name := "Gopher"
	message := greet(name)
	fmt.Println(message)

	currentTime := time.Now()
	fmt.Printf("Current time is: %s\n", currentTime.Format("15:04:05"))
}
