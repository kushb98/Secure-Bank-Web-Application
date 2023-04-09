from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
import re


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    #query ="""SELECT E.ID as employee_id, first_name, last_name, company_id, email, C.name FROM IS601_MP3_Employees E LEFT JOIN #IS601_MP3_Companies C ON E.company_id = C.id"""
    query ="""SELECT E.ID as Employee_id , first_name , last_name , company_id, email , C.name as Company_name FROM IS601_MP3_Employees E LEFT JOIN IS601_MP3_Companies C ON E.company_id = C.id WHERE 1=1 """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name= request.args.get("fname")
    last_name = request.args.get("lname")
    email = request.args.get("email")
    company= request.args.get("company")
    col =  request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")

    employee_dict={}
    
    #if(request.args.get("field")):
    #    employee_dict["col"] = col
    #    query= query+ """ AND (first_name = %(col)s OR last_name= %(col)s OR email = %(col)s OR company= %(col)s)"""
    
    # TODO search-3 append like filter for first_name if provided
    if(first_name != ""):
        employee_dict["first_name"] = "%"+str(first_name)+"%"
        query += " AND first_name like %s"
        query= query+ """ AND first_name like %(first_name)s """
    # TODO search-4 append like filter for last_name if provided
    if(last_name != ""):
        employee_dict["last_name"] = "%"+str(last_name)+"%"
        query += " AND last_name like %s"
        query= query+ """ AND last_name like %(last_name)s """

    # TODO search-5 append like filter for email if provided
    if(email != ""):
        employee_dict["email"] = email
        query= query+ """ AND email like %(email)s """

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND company_id=%s"
        query = query+ """ AND company_id = %(company_id)s"""
        employee_dict["company_id"] = company

    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    print("-------------------------------------------------------------------")
    print(col)
    print(order)

    if col and order:
            if col in allowed_columns and order in ["asc", "desc"]:    
                #query = query + """ORDER BY %(col_name)s %(order)s"""
                query = query + " ORDER BY {} {}".format(col.lower(), order.lower())
                employee_dict["col_name"] = col.lower()
                employee_dict["order"] = order.lower()
                print("-------------------------------------------------------------------")
                print(query)
            

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if(limit!=None):
        if(int(limit) > 0 and int(limit) <= 100):
            query = query+ " LIMIT %(limit)s"
            employee_dict["limit"] = int(limit)
        else:
            print("Limit is out of bound, please enter values greater than 0 and less than 101")
            flash("Limit out of bound(1 to 100) or not selected","warning")
    else:
        print("Entered value is not integer, Please enter a valid integer value")

    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    args = employee_dict # <--- add values to replace %s/%(named)s placeholders

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash("Error!! - Cannot fetch the required data", "Danger")
        print(str(e))
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation

    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        #kb97 | 8th April 2023
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        company_id = request.form.get("company")

        # TODO add-2 first_name is required (flash proper error message)
        #kb97 | 8th April 2023
        if len(first_name) == 0:
            flash("First Name field is required","warning")

        # TODO add-3 last_name is required (flash proper error message)
        #kb97 | 8th April 2023
        if len(last_name) == 0:
            flash("Last Name field is required","warning")

        # TODO add-4 company (may be None)
        #kb97 | 8th April 2023
        
        # TODO add-5 email is required (flash proper error message)
        #kb97 | 8th April 2023
        if len(email) == 0:
            flash("Email field is required","warning")

        # TODO add-5a verify email is in the correct format
        #kb97 | 8th April 2023
        email_format = r"[^@]+@[^@]+\.[^@]+"
        if re.match(email_format, email) is None == False:
            flash("Email is not in correct format.","warning")
        has_error = False # use this to control whether or not an insert occurs

        employee_dict={}
        employee_dict["first_name"] = first_name
        employee_dict["last_name"] = last_name
        employee_dict["email"] = email
        employee_dict["company_name"]= company_id
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company_name)s)
                    ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                    last_name = %(last_name)s, email = %(email)s, 
                    company_id = %(company_name)s""",employee_dict
                ) # <-- TODO add-6 add query and add arguments
                #kb97 | 8th April 2023
                if result.status:
                    flash("Employee Record Created Successfully!", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash("Employee Record Creation Failed!", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs

            
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE ... SET
                    ...
                    """, ...)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(e, "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""SELECT 
            ...
            FROM ... LEFT JOIN ... 
            
            WHERE ..."""
            , id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", ...)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    pass