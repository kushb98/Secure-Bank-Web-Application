from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
import re


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    #UCID: kb97 Date: 8th April 2023
    query = """SELECT E.ID as id , first_name , last_name , company_id, email , C.name as Company_name 
                FROM IS601_MP3_Employees E LEFT JOIN IS601_MP3_Companies C ON E.company_id = C.id WHERE 1=1 """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    #UCID: kb97 Date: 8th April 2023
    fn =  request.args.get("fname")
    ln =  request.args.get("lname")
    email = request.args.get("email")
    company_id = request.args.get("company")
    col =  request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")
    
    employee_dict = {}
    # TODO search-3 append like filter for first_name if provided
    #UCID: kb97 Date: 8th April 2023
    if(fn != ""):
        employee_dict["first_name"] = "%"+str(fn)+"%"
        query = query+ """ AND first_name like %(first_name)s """
    # TODO search-4 append like filter for last_name if provided
    #UCID: kb97 Date: 8th April 2023
    if(ln != ""):
        employee_dict["last_name"] = "%"+str(ln)+"%"
        query= query+ """ AND last_name like %(last_name)s """
    # TODO search-5 append like filter for email if provided
    #UCID: kb97 Date: 8th April 2023
    if(email != ""):
        employee_dict["email"] = email
        query= query+ """ AND email like %(email)s """
    # TODO search-6 append equality filter for company_id if provided
    #UCID: kb97 Date: 8th April 2023
    if company_id:
        query = query+ """ AND company_id = %(company_id)s"""
        employee_dict["company_id"] = company_id
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    #UCID: kb97 Date: 8th April 2023
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
    #UCID: kb97 Date: 9th April 2023
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
    #UCID: kb97 Date: 9th April 2023
    
    args = employee_dict # <--- add values to replace %s/%(named)s placeholders 
            
    #limit = 10 # TODO change this per the above requirements
    #query += " LIMIT %(limit)s"
    #args["limit"] = limit
    print("query",query)
    print("args", args)
    print(fn)
        
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        #UCID: kb97 Date: 9th April 2023
        flash("Not able to fetch the data", "error")
        print(str(e))
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    allowed_columns = [(v,v) for v in allowed_columns]
    # do this prior to passing to render_template, but not before otherwise it can break validation
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        
        fn = request.form.get("first_name")
        ln = request.form.get("last_name")
        company = request.form.get("company",None)
        email = request.form.get("email")
        if fn=="":
            flash("First name is a required field!", "danger")
            return redirect(url_for("employee.add"))
        if ln=="":
            flash("Last Name is a required field", "danger")
            return redirect(url_for("employee.add"))
        if email=="":
            flash("Email is a required field", "danger")
            return redirect(url_for("employee.add"))
        
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if re.match(email_regex, email) is not None == False:
            flash("Email is not in valid format!","warning")

        has_error = False # use this to control whether or not an insert occurs
        if not has_error:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP3_Employees (first_name, last_name,company_id,email) VALUES(%s, %s, %s, %s)",fn, ln,company,email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Employee Record Created Successfully!", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash("Employee cannot be added", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    print("++++++++++++++++++++++++++++++++++++")
    id = False
    #Below line is printing NONE value idk why its not retrieving the value::::::Need to check)
    id = request.args.get("id")
    print(id)
    if not id: # TODO update this for TODO edit-1
        flash("Company id is NULL","warning")
        return redirect(url_for("employee.search"))
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            company = request.form.get("company")
            email = request.form.get("email")
                
            # TODO edit-2 first_name is required (flash proper error message)
            if(first_name==""):
                flash("First Name field is required","warning")
                has_error = True
            # TODO edit-3 last_name is required (flash proper error message)
            if(last_name==""):
                flash("Last Name field is required","warning")
                has_error = True
            # TODO edit-4 company (may be None)
            #flash("Company field is optional")
            # TODO edit-5 email is required (flash proper error message)
            if(email==""):
                flash("Email field is required","warning")
                has_error = True
            # TODO edit-5a verify email is in the correct format
            email_check = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if re.match(email_check,email):
                pass
            else:
                flash("Email is not in correct format", "danger")
                has_error = True
            has_error = False # use this to control whether or not an insert occurs

            employee_dict={}
            employee_dict["first_name"] = first_name
            employee_dict["last_name"] = last_name
            employee_dict["email"] = email
            employee_dict["company_name"]= company
            employee_dict["e_id"]= id
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""UPDATE IS601_MP3_Employees SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, company_id=%(company_name)s WHERE id=%(e_id)s
                    """, employee_dict)
                    if result.status:
                        flash("Record Updated Successfully!", "success")
                    return redirect(url_for('employee.search', first_name="", last_name="", email="", company="", order="asc", column="", limit=10))
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash("Error!!The updation of the database failed", "danger")
                    print(str(e))
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP3_Employees employees LEFT JOIN IS601_MP3_Companies companies ON employees.company_id=companies.id WHERE employees.id=%s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Error occured! The data cannot be retrived", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html",employee=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    id = request.args.get("id")
    # make a mutable dict
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
            if result.status:
                flash("Record Deleted Successfully!", "success")
        except Exception as e:
            # TODO make this user-friendly
            flash("Data cannot be deleted", "danger")
        # TODO pass along feedback

        # remove the id args since we don't need it in the list route
        # but we want to persist the other query args
        del args["id"]
    return redirect(url_for("employee.search", **args))
    