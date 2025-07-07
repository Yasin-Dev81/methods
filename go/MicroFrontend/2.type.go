// اگه متغیری تعریف بشه و استفاده نشه ارور میده!
package main

// ماژول فرمتینگ
import "fmt"

func main() {
	// تعریف متغیر
	// default = 0
	var x int
	var y int = 3
	// تنظیم تایپ براساس مقدار اولیه
	var a = 10
	b := 10
	// تنظیم چندتایی
	var (
		c = 2
		d = "hi"
	)
	print(x, y, a, b, c, d)

	// دیدن آدرس یه متغیر
	fmt.Println(&a)
}
