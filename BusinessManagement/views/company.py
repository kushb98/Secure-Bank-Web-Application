from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *

    query = """SELECT id, name, address, city, country , state, zip, website, (SELECT count(id) FROM IS601_MP3_Employees WHERE c.id=company_id GROUP BY company_id)
        as employees from IS601_MP3_Companies as c WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    state = request.args.get("state")
    country = request.args.get("country")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")

    company_dict={}
    # TODO search-3 append a LIKE filter for name if provided
    if(name != ""):
        company_dict["name"] = "%"+str(name)+"%"
        query= query+ """ AND name like %(name)s """
    # TODO search-4 append an equality filter for country if provided
    if country:
        query = query+ """ AND country = %(country)s"""
        company_dict["country"] = country
    # TODO search-5 append an equality filter for state if provided
    if state:
        query = query+ """ AND state = %(state)s"""
        company_dict["state"] = state
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            #query = query + """ORDER BY %(col_name)s %(order)s"""
            query = query + " ORDER BY {} {}".format(column.lower(), order.lower())
            company_dict["col_name"] = column.lower()
            company_dict["order"] = order.lower()
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    #limit = 10
    if(limit!=None):
        if(int(limit) > 0 and int(limit) <= 100):
            query = query+ " LIMIT %(limit)s"
            company_dict["limit"] = int(limit)
        else:
            print("Limit is out of bound, please enter values greater than 0 and less than 101")
            flash("Limit out of bound(1 to 100) or not selected","warning")
    else:
        print("Entered value is not integer, Please enter a valid integer value")
    
    args = company_dict

    #limit = 10 # TODO change this per the above requirements
    #query += " LIMIT %(limit)s"
    #args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash("Error!! - Cannot fetch the required data", "Danger")
        print(str(e))
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(v,v) for v in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name", None)
        address = request.form.get("address", None)
        city = request.form.get("city", None)
        website = request.form.get("website", None)
        state = request.form.get("state", None)
        country = request.form.get("country", None)
        zip_code = request.form.get("zipcode", None)
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-2 name is required (flash proper error message)
        if len(name) == 0:
            has_error = True
            flash("Name is a required field!","warning")
        # TODO add-3 address is required (flash proper error message)
        if len(address) == 0:
            has_error = True
            flash("Address is a required field!","warning")
        # TODO add-4 city is required (flash proper error message)
        if len(city) == 0:
            has_error = True
            flash("City is a required field!","warning")
        # TODO add-5 state is required (flash proper error message)
        if len(state) == 0:
            has_error = True
            flash("State is a required field!","warning")
        # TODO add-6 country is required (flash proper error message)
        if len(country) == 0:
            has_error = True
            flash("Country is a required field!","warning")
        # TODO add-7 website is not required
        flash("Website is an optional field","")

        if not has_error:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP3_Companies (name,address,city,country,state,zip,website) VALUES (%s,%s,%s,%s,%s,%s,%s)",name,address,city,country,state,zip_code,website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Company added successfully!", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Something went wrong their was error creating the company","danger")
                flash(str(e), "danger")

    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #id = False
    id = request.args.get("id")
    print(id)
    if not id: # TODO update this for TODO edit-1
        flash("Cannot fetch id...redirecting to search page","warning")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip")
            website = request.args.get("website")
            if(request.form.get("website")):
                website = request.form.get("website")

            # TODO edit-2 name is required (flash proper error message)
            if(name==""):
                flash("Name cannot be empty ","danger")
                has_error = True
            # TODO edit-3 address is required (flash proper error message)
            if(address==""):
                flash("Address cannot be empty ","danger")
                has_error = True
            # TODO edit-4 city is required (flash proper error message)
            if(city==""):
                flash("City cannot be empty ","danger")
                has_error = True
            # TODO edit-5 state is required (flash proper error message)
            if(state==""):
                flash("State cannot be empty ","danger")
                has_error = True
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            if(country==""):
                flash("Country cannot be empty ","danger")
                has_error = True
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            flash("Website is optional ","warning")
            # TODO edit-8 zipcode is required (flash proper error message)
            if(zipcode==""):
                flash("Zip cannot be empty ","danger")
                has_error = True
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs
            
            data["name"] = name
            data["address"] = address
            data["city"] = city
            data["website"]= website
            data["state"]= state
            data["country"] = country
            data["zipcode"]= zipcode
            data["c_id"]=id
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""UPDATE IS601_MP3_Companies SET name=%(name)s, address=%(address)s, city=%(city)s, website=%(website)s, state=%(state)s, country=%(country)s, zip=%(zipcode)s  WHERE id=%(c_id)s
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                    return redirect(url_for('company.search', name="", order="asc", column="", limit=10))
                    
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash("Error!!The updation of the database failed", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT id, name, address, city, country , state, zip, website FROM IS601_MP3_Companies WHERE id=%s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Error occured! The data cannot be retrived", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html",company=row)