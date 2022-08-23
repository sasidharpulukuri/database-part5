import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user ="spulukuri",
      password="S4567",
      host ="127.0.0.1",
      port="3306",
      database="teaproject")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   print("...Execute database operations.....")
   # Execute database operations...

   my_cursor = cm_connection.cursor()

   player_query = ("SELECT customer_id, customer_name,customer_address,phone_number FROM customer_details")

   my_cursor.execute(player_query)


   # Display results
   for row in my_cursor.fetchall():
      print("{}   {} {} {}".format(row[0], row[1], row[2], row[3]))
   my_cursor.close()
   # displaying particular record
   customer_cursor = cm_connection.cursor()
   customer_query = ("SELECT order_details.order_id,order_status.order_id,order_details.order_date")
   customer_query += (" FROM order_details JOIN order_status on order_details.order_id = order_status.order_id")
   customer_query += (" WHERE order_details.order_id = %s")

   rep_last = input("Enter orderid(order_id) ")

   rep_data = (rep_last,)  # Comma required for single value tuple
   customer_cursor.execute(customer_query, rep_data)
   for row in customer_cursor.fetchall():
      print("{} {} {} ".format(row[0], row[1], row[2]))
      customer_cursor.close()
      print("This is example is more complex. It uses functions, dictionaries and conditionals")
      # This is example is more complex. It uses functions, dictionaries and conditionals.

      import mysql.connector
      from mysql.connector import errorcode


      def get_status():
         statuses = {1: "Shipped", 2: "Resolved", 3: "Cancelled", 4: "On Hold", 5: "Disputed", 6: "In Process"}
         for key in statuses:
            print("{}. {}".format(key, statuses[key]))
         status = int(input("Enter status number or 0 for all orders: "))
         if 0 < status <= 6:
            return statuses[status]
         else:
            return "all"


      # main program

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="spulukuri",
            password="S4567",
            host="127.0.0.1",
            port="3306",
            database="teaproject")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         order_status = get_status()

         orders_cursor = cm_connection.cursor()
         orders_query = ("SELECT *")
         orders_query += ("FROM order_status")

         if order_status == "all":
            print("\n**All Orders**")
            print("{} {} {}".format("order_status_id", "order_id", "process"))
            print("-" * 77)
            orders_cursor.execute(orders_query)
            for (order_status_id, order_id, process) in orders_cursor:
               print("{} {} {}".format(order_status_id, order_id, process), end="")
            # if shippedDate is None:
            #    print(" Not Shipped", end="")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate), end="")
            print(" {}".format(process))
         else:
            orders_query += (" WHERE process = %s")
            status_data = (order_status,)
            orders_cursor.execute(orders_query, status_data)
            print("\n**Status: {}**".format(order_status))
            print("{} {} {}".format("order_status_id", "order_id", "process"))
            for (order_status_id, order_id, process) in orders_cursor:
               print("{} {} {}\n".format(order_status_id, order_id, process), end="",)
            # if shippedDate is None:
            #    print(" Not Shipped")
            # else:
            #    print(" {:%m/%d/%Y} ".format(shippedDate))

         orders_cursor.close()
         cm_connection.close()

         # Example of displaying a one-to-many relationship
         print(".....Example of displaying a one-to-many relationship.......")
         import mysql.connector
         from mysql.connector import errorcode

         # connect to DB
         try:
            cm_connection = mysql.connector.connect(
               user="spulukuri",
               password="S4567",
               host="127.0.0.1",
               port="3306",
               database="teaproject")

         except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
               print("Invalid credentials")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
               print("Database not found")
            else:
               print("Cannot connect to database:", err)

         else:
            select_clause = "SELECT order_details.customer_id,customer_details.customer_id"
            from_clause = "FROM order_details  JOIN customer_details on order_details.customer_id = customer_details.customer_id"
            # from_clause += " JOIN order_details  ON order_details.customer_id = customer_details.customer_id"
            where_clause = "WHERE customer_name = 'tom' and customer_address='street gh'"
         order_clause = "ORDER BY customer_name"
         orders_query = "{} {} {} {}".format(select_clause, from_clause, where_clause, order_clause)

         orders_cursor = cm_connection.cursor()
         orders_cursor.execute(orders_query)

         prev_orderNumber = ""  # identifies new order
         for (customer_id, customer_name) in orders_cursor:
            if customer_id != prev_orderNumber:
               prev_orderNumber = customer_id
               print("\ncustomer id: {} required by {}".format(customer_id, customer_name))
               print("customer id")
               print("   {}".format(customer_id))
               # print("   {}".format(customer_name))

               print("Ordered by")
         print("  {}  ".format(customer_name))

   # Insert an customer
      print(".....Insert an customer.....")
      import mysql.connector
      from mysql.connector import errorcode
      import random

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="spulukuri",
            password="S4567",
            host="127.0.0.1",
            port="3306",
            database="teaproject")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         office_query = "SELECT customer_id,customer_name FROM customer_details"
         office_cursor = cm_connection.cursor()
         office_cursor.execute(office_query)
         for row in office_cursor.fetchall():
            print("{}. {}".format(row[0], row[1]))
         office_cursor.close()

         ci = input("Enter customer id ")
         cn = input("Enter customer name: ")
         ca = input("Enter customer address ")
         pn = input("Enter phone no ")


         employee_query = ("INSERT INTO customer_details "
                           "(customer_id,customer_name,customer_address,phone_number)"
                           "VALUES (%s, %s, %s, %s)")

         employee_data = (ci,cn,ca,pn)
         try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            cm_connection.commit()
            print("Added customer")
            employee_cursor.close()
         except mysql.connector.Error as err:
          print("\nEmployee not added")
          print("Error: {}".format(err))
      cm_connection.close()
print("......Update an customer.......")
# Update an customer
import mysql.connector
from mysql.connector import errorcode


try:
   cm_connection = mysql.connector.connect(
      user="spulukuri",
      password="S4567",
      host="127.0.0.1",
      port="3306",
      database="teaproject")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   employee_last = input("Enter customer_id ")
   column = input("Enter item to update (customer_id, customer_name, customer_address, phone_number) ")
   prompt = "Enter new value for {} ".format(column)
   value = input(prompt)

   employee_query = ("UPDATE customer_details "
                     "SET " + column + " =  %s "
                                       "WHERE customer_id = %s")
   employee_data = (value, employee_last)
   try:
      employee_cursor = cm_connection.cursor()
      employee_cursor.execute(employee_query, employee_data)
      cm_connection.commit()
      print("Updated employee")
      employee_cursor.close()
   except mysql.connector.Error as err:
    print("\nEmployee not updated")
    print("Error: {}".format(err))
    cm_connection.close()

   # Delete an customer
   print("Delete an customer")
   import mysql.connector
   from mysql.connector import errorcode

   # connect to DB
   try:
      cm_connection = mysql.connector.connect(
         user="spulukuri",
         password="S4567",
         host="127.0.0.1",
         port="3306",
         database="teaproject")

   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Invalid credentials")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database not found")
      else:
         print("Cannot connect to database:", err)

   else:
      employee_last = input("Enter customer id to delete ")

      employee_query = ("DELETE FROM customer_details "
                        "WHERE customer_id = %s")
      employee_data = (employee_last,)
      try:
         employee_cursor = cm_connection.cursor()
         employee_cursor.execute(employee_query, employee_data)
         cm_connection.commit()
         print("Deleted customer")
         employee_cursor.close()
      except mysql.connector.Error as err:
         print("\ncustomer not updated")
         print("Error: {}".format(err))
      cm_connection.close()

print("Sucess!")
cm_connection.close()