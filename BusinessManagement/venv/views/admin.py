import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No file was selected!', "warning")
            return redirect(request.url)
        
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not

        #kb97 | 8th April 2023 
        if '.csv' not in file.filename:
            flash('The file is not a .csv file!',"danger")
            return redirect(request.url)

        if file and secure_filename(file.filename):
            companies = []
            employees = []
            # DON'T EDIT
            company_query = """
            INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website)
            """
            # DON'T EDIT
            employee_query = """
            INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, 
                        company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            #kb97 | 8th April 2023
            
            import csv
            csv_reader = csv.DictReader(stream)
            for row in csv_reader:
                company_dict={}
                employee_dict={}
                
                if row["first_name"] and row["last_name"] and row["email"] and row["company_name"]:
                    employee_dict["first_name"] = row.get("first_name")
                    employee_dict["last_name"] = row.get("last_name")
                    employee_dict["email"] = row.get("email")
                    employee_dict["company_name"] = row.get("company_name")
                    employees.append(employee_dict)
                
                if row["company_name"] and row["address"] and row["city"] and row["country"] and row["state"] and row["zip"] and row["web"]:
                    company_dict["name"] = row.get("company_name")
                    company_dict["address"] = row.get("address")
                    company_dict["city"] = row.get("city")
                    company_dict["country"] = row.get("country")
                    company_dict["state"] = row.get("state")
                    company_dict["zip"] = row.get("zip")
                    company_dict["website"] = row.get("web")
                    companies.append(company_dict)            
                
                
                # print(row) #example
                #kb97 | 8th April 2023
                # TODO importcsv-3 extract company data and append to company list 
                # as a dict only with company data if all is present
                #kb97 | 8th April 2023
                # TODO importcsv-4 extract employee data and append to employee list 
                # as a dict only with employee data if all is present
                
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    #kb97 | 8th April 2023
                    flash(f"{len(companies)} rows are inserted for companies successfully","success")                    
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                #kb97 | 8th April 2023
                flash("No companies were loaded", "warning")                
                pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    #kb97 | 8th April 2023
                    flash(f"{len(employees)} rows are inserted for employee","success")                    
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no employees were loaded
                #kb97 | 8th April 2023
                flash("No employees were loaded","warning")                
                pass
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                    traceback.print_exc()
                    flash("There was an error counting session queries", "danger")
    return render_template("upload.html")
