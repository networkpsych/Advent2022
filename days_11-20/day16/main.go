package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
)

type Elfs struct {
	Elfs []Elf `json:"valves"`
}

type Elf struct {
	Name    string `json:"name"`
	Flow    int    `json:"flow"`
	Tunnels string `json:"tunnels"`
}

func main() {

	jsonFile, err := os.Open("tunnel.json")
	if err != nil {
		fmt.Println(err)
	}
	defer jsonFile.Close()

	byteVal, err2 := io.ReadAll(jsonFile)
	if err2 != nil {
		fmt.Println(err2)
	}

	var elf Elfs
	json.Unmarshal(byteVal, &elf)

	for i := 0; i < len(elf.Elfs); i++ {
		if elf.Elfs[i].Flow > 5 {
			fmt.Printf("Valve: %s\tFlow:%d\tTunnels:%s\t\n",
				elf.Elfs[i].Name, elf.Elfs[i].Flow, elf.Elfs[i].Tunnels)
		}
	}
}
