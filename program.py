MAVEN COMMAND
1)mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
2)mvn package 
3)java -cp target/my-app-1.0-SNAPSHOT.jar com.example.App



MAKE CHANGES TO FILES IN DIFFERENT BRANCHES AND PERFORM PULL REQUESTS AND MERGING 

1.cd desktop
2.cd OSTlab
3.git clone https://github.com/Deepika0422/OSTlab.git
4.git init
5.git checkout -b branch1
Cd os
git clone gitlink
git init
git checkout -b b1
6.git add text1.txt
7.git commit -m "Change made successfully"
8.git branch
9.git remote add origin https://github.com/Deepika0422/OSTlab.git
10.git push origin branch1
11.git checkout -b main
12.git add text2.txt
13.git commit -m "new change"
14.git push origin main


BASIC OPERATIONS 
Here is the revised Java program:

```
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        while (true) {
            System.out.println("Choose an operation:");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Modulo Division");
            System.out.println("6. Exit");

            System.out.print("Enter your choice (1-6): ");
            int choice = scanner.nextInt();

            if (choice == 6) {
                System.out.println("Exiting...");
                break;
            }

            switch (choice) {
                case 1:
                    System.out.println("Result: " + add(num1, num2));
                    break;
                case 2:
                    System.out.println("Result: " + subtract(num1, num2));
                    break;
                case 3:
                    System.out.println("Result: " + multiply(num1, num2));
                    break;
                case 4:
                    if (num2 != 0) {
                        System.out.println("Result: " + divide(num1, num2));
                    } else {
                        System.out.println("Error! Division by zero is not allowed.");
                    }
                    break;
                case 5:
                    if (num2 != 0) {
                        System.out.println("Result: " + modulo(num1, num2));
                    } else {
                        System.out.println("Error! Modulo division by zero is not allowed.");
                    }
                    break;
                default:
                    System.out.println("Invalid choice. Please choose a valid option.");
            }
        }
    }

    public static double add(double num1, double num2) {
        return num1 + num2;
    }

    public static double subtract(double num1, double num2) {
        return num1 - num2;
    }

    public static double multiply(double num1, double num2) {
        return num1 * num2;
    }

    public static double divide(double num1, double num2) {
        return num1 / num2;
    }

    public static double modulo(double num1, double num2) {
        return num1 % num2;
    }
}


DATA ENGINEERING PROJECT
Program:
1. Data Ingestion Module (DataIngestion.java):
 Reads and parses a CSV file.
 package com.example.dataengineering.ingestion;
 import java.io.*;
 import java.util.*;
 public class DataIngestion {
 public List<String[]> readCSV(String filePath) {
 List<String[]> data = new ArrayList<>();
 try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
 String header = br.readLine(); // Skip header
 String line;
 while ((line = br.readLine()) != null) {
 data.add(line.split(","));
 }
 } catch (IOException e) {
 e.printStackTrace();
 }
 return data;
 }
 }
2. Data Transformation Module (DataTransformation.java):
 Filters rows based on criteria.
 
 package com.example.dataengineering.transformation;
 import java.util.*;
 public class DataTransformation {
 public List<String[]> filterByCountry(List<String[]> data, String country) {
 return data.stream().filter(row -> row[2].equalsIgnoreCase(country))
 .collect(Collectors.toList());
 }
 }
 
3. Data Storage Module (DataStorage.java):
 Writes processed data to a file.
 
 package com.example.dataengineering.storage;
 import java.io.*;
 import java.util.*;
 public class DataStorage {
 public void writeCSV(List<String[]> data, String outputPath) {
 try (FileWriter writer = new FileWriter(outputPath)) {
 for (String[] row : data) {
 writer.append(String.join(",", row)).append("\n");
 }
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
 }
 
4. Data Analytics Module (DataAnalytics.java):
 Computes analytical metrics.
 
 package com.example.dataengineering.analytics;
 import java.util.*;
 public class DataAnalytics {
 public double calculateAverageSalary(List<String[]> data) {
 return data.stream()
 .mapToDouble(row -> Double.parseDouble(row[4]))
 .average()
 .orElse(0);
 }
 }
 
5. Main Class (Main.java):
 Integrates all modules.
 
 package com.example;
 import com.example.dataengineering.ingestion.*;
 import com.example.dataengineering.transformation.*;
 import com.example.dataengineering.storage.;import com.example.dataengineering.analytics.;
 import java.util.*;
 public class Main {
 public static void main(String[] args) {
 String inputFile = "data/input.csv";
 String outputFile = "data/output.csv";
 DataIngestion ingestion = new DataIngestion();
 DataTransformation transformation = new DataTransformation();
 DataStorage storage = new DataStorage();
 DataAnalytics analytics = new DataAnalytics();
 List<String[]> data = ingestion.readCSV(inputFile);
 List<String[]> filteredData = transformation.filterByCountry(data, "USA");
 storage.writeCSV(filteredData, outputFile);
 double avgSalary = analytics.calculateAverageSalary(filteredData);
 System.out.println("Average Salary in the USA: $" + avgSalary);
 }
 }
WEB APPLICATIONS 
HelloServlet.java
___
package com.example;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("text/html");
        resp.getWriter().println("<h1>Hello, World!</h1>");
    }
}
____
Web.xml
____
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">

    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>

</web-app>
____
Index.html
____
<html>
    <head>
        <title>Events</title>
        <link rel="icon" href="images/img1.jpeg">
    </head>
    <body bgcolor="black" style="color: white;">
        <h1 align="center">Upcoming Events &#x1F4C6</h1>
        <h4 align="center">Don't miss any of your events.Here are the important events you have registered for! </h4>
        <hr>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed cumque cum soluta, incidunt libero quasi est eaque voluptatibus vitae illo eveniet, nihil assumenda! Nesciunt debitis libero quia cum perferendis, sint earum molestiae dolores doloribus voluptatem illo neque non commodi facilis consequatur ut nemo. Dicta nemo nulla minima eum totam quibusdam, earum quidem sed consectetur pariatur sunt suscipit at! Mollitia veniam, officia debitis velit iusto iure voluptas quo odio fugiat ea magni reiciendis, possimus voluptatem reprehenderit dolorem optio repudiandae dignissimos ab facere voluptates facilis eligendi qui nulla modi! Officiis minus, ad excepturi pariatur sit exercitationem fuga consequuntur repellat quis, eveniet quos.</p>

        <p align="center"><img src="images/img2.jpeg"></p>
        <h1 align="center">Photo Gallery Event</h1>
        <h2 align="center"> Free Entry | Free Food | Pets are Not Allowed</h2>
        <p align="center">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Est a harum accusantium corrupti quisquam, nisi sit officiis. Cum culpa iusto obcaecati autem tenetur excepturi voluptas illo aspernatur vel, quae voluptates non alias eum eaque voluptatum dolorem exercitationem adipisci a dicta praesentium! Tenetur in assumenda ducimus, nulla fuga est rerum cumque?</p>
        <p align="center"><img src="images/img3.jpeg"></p>
        <p align="center"><a href="https://www.flipkart.com/" target="box">Fashion Store</a></p>
        <p align="center"> <iframe name="box" height="600px" width="800px" src="images/man.gif" >Here you go!</iframe></p>
        <h3 align="center"> Free Entry | Free Food | Pets are Not Allowed</h3>
        <p align="center">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odio possimus eos exercitationem. Pariatur eius, voluptatum laudantium dolore laborum eos quibusdam quasi, alias sint ipsam labore.</p>
        <hr>
<h1 align="center">Contact</h1>
<h2 align="center">+91 65926526899| eventcollab@gmail.com</h2>
<h3 align="center">9th street Avenue Park,Salem,636304</h3>
<h2 align="center"><a href="Register.html" target="_blank">Resister Now!</a></h2>


    </body>
</html>
_____
register.html
____
<style>
    label{
        color:rgb(16, 23, 16);
        font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif ;
        
    }
</style>


<html>
    <head>
        <title>FormTag</title>
    </head>
    <body  background="images/earth.png" >
        <h1 align="center"style="color:blue">Basics</h1>
        <h1 align="center" style="color:blue">Form Tag</h1>
        <center>
        <fieldset >
            <legend><h1 style="color:rgb(188, 79, 192)">Register Form</h1></legend>
            
            <form>
                <table>
               <tr>
                <td><label>NAME :</label></td>
                <td><input type="text" placeholder="Your name" style="background:lightblue;" ><br><br></td>
            </tr>
            <tr>
                <td> <label>PASSWORD:</label></td>
                    <td><input type="password" style="background:lightblue;"><br><br></td>
                </tr>
                <tr>
                <td><label>DOB :</label></td>
                <td><input type="date" style="background:lightblue;"><br><br></td>
            </tr>
            <tr>
               <td> <label>ADDRESS :</label><br><br></td>
                <td><textarea  cols="60" rows="5" style="background:lightblue;"></textarea><br><br></td>
            </tr>
            <tr>
              <td>  <label>GENDER :</label></td>
               <td > <input type="radio" name="gen"  >MALE
                <input type="radio" name="gen">FEMALE
                <br><br></td>
            </tr>
            <tr>
                <td><label>COURSE:</label></td>
                <td><select style="background:lightblue;" > 
                    <option value="1" >DLD</option> 
                    <option value="2" >DSA</option> 
                    <option value="3" >FDS</option> 
                     </select>
                     <br><br></td>
                    </tr>
                    <tr>
                     <td><label>FILES:</label></td>
                    <td> <input type="file" style="background:lightblue;"><br><br></tr>
                    </tr>
                    <tr>
                      <td></td><td> <button style="background:lightblue;">SUBMIT</button>
                      <button style="background:lightblue;">RESET</button></td>
                    </tr>
                    </table>
                    <h2>
                        <a href="index.html">Home |</a>
                        <a href="https://google.com" target="_blank">Google</a>
                    
                    </h2>
            </form>
        
        </fieldset>
    </center>
    </body>
</html>

SCALA ABSTRACT CLASS
// Abstract Class: Animal
abstract class Animal(val name: String) {
 def sound(): Unit
 // Primary constructor
 // Auxiliary constructor
 def this() = this("Unknown")
 def eat(): Unit = println(s"$name is eating...")
}
// Trait: Mammaltrait Mammal {
 def nurse(): Unit = println("Nursing...")
}
// Trait: Pet
trait Pet {
 def play(): Unit = println("Playing...")
}
// Concrete Class: Dog
class Dog(val breed: String) extends Animal(breed) with Mammal with Pet {
 override def sound(): Unit = println("Woof!")
 override def eat(): Unit = println(s"$breed is eating...")
 // Auxiliary constructor
 def this() = this("Golden Retriever")
}
// Concrete Class: Cat
class Cat(val color: String) extends Animal(color) with Mammal with Pet {
 override def sound(): Unit = println("Meow!")
 override def eat(): Unit = println(s"$color is eating...")
 // Auxiliary constructor
 def this() = this("Black")
}
// Companion Object: Dog
object Dog {
 def apply(): Dog = new Dog()
}
// Companion Object: Cat
object Cat {
 def apply(): Cat = new Cat()
}
// Singleton Object: AnimalKingdom
object AnimalKingdom {
 def main(args: Array[String]): Unit = {val dog = new Dog("Poodle")
 dog.sound()
 dog.eat()
 dog.nurse()
 dog.play()
 val defaultDog = Dog()
 defaultDog.sound()
 defaultDog.eat()
 defaultDog.nurse()
 defaultDog.play()
 val cat = new Cat("White")
 cat.sound()
 cat.eat()
 cat.nurse()
 cat.play()
 val defaultCat = Cat()
 defaultCat.sound()
 defaultCat.eat()
 defaultCat.nurse()
 defaultCat.play()
 }
}

<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example.dataengineering</groupId>
        <artifactId>data-engineering-parent</artifactId>
        <version>1.0-SNAPSHOT</version>
        <relativePath>../pom.xml</relativePath> <!-- Points to parent POM -->
    </parent>

    <artifactId>data-ingestion</artifactId>
    <dependencies>
        <!-- Add specific ingestion-related dependencies -->
        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>kafka-clients</artifactId>
            <version>2.6.0</version>
        </dependency>
<dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
        <scope>test</scope>
    </dependency>
<dependency>
        <groupId>com.example.dataengineering</groupId>
        <artifactId>data-transformation</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.example.dataengineering</groupId>
        <artifactId>data-storage</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.example.dataengineering</groupId>
        <artifactId>data-analytics</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>

        <!-- Add other ingestion-related dependencies -->
    </dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.4.0</version>
            <executions>
                <execution>
                    <goals>
                        <goal>java</goal>
                    </goals>
                </execution>
            </executions>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>

</project>
