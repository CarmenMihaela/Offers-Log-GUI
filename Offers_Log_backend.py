import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute ("CREATE TABLE IF NOT EXISTS entry (id INTEGER PRIMARY KEY, no text, client text, item_requested text, quote_status text, offer_manager text, sales_manager text, cost_meur integer, comments text )")
        self.conn.commit()

    def insert(self, no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur, comments_text):
        self.cur.execute ("INSERT INTO entry VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur, comments_text))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM entry")
        rows = self.cur.fetchall()
        return rows

    # def search(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
    #     self.cur.execute("SELECT * FROM entry WHERE no = ? OR client = ? OR item_requested = ? OR quote_status = ? "
    #                      "OR offer_manager = ? OR sales_manager = ? OR cost_meur = ? ",
    #                      (no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur))
    #     rows = self.cur.fetchall()
    #     return rows

    # def search(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
    #     self.cur.execute("SELECT * FROM entry WHERE no = ? OR client = ? OR item_requested = ? OR quote_status = ? "
    #                      "OR offer_manager = ? OR sales_manager = ? OR cost_meur = ? ",
    #                      (no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur))
    #     rows = self.cur.fetchall()
    #     return rows

# single field search:

    def search1(self, no = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ?", (no,))
        rows = self.cur.fetchall()
        return rows

    def search11(self, client = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ?", (client,))
        rows = self.cur.fetchall()
        return rows

    def search111(self, item_requested = ""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ?", (item_requested,))
        rows = self.cur.fetchall()
        return rows

    def search1111(self, quote_status = ""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ?", (quote_status,))
        rows = self.cur.fetchall()
        return rows

    def search11111(self, offer_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE offer_manager = ?", (offer_manager,))
        rows = self.cur.fetchall()
        return rows


    def search111111(self, sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE sales_manager = ?", (sales_manager,))
        rows = self.cur.fetchall()
        return rows

    def search1111111(self, cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE cost_meur = ?", (cost_meur,))
        rows = self.cur.fetchall()
        return rows

# 2 fields search:
    def search2(self, no = "", client = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ?", (no, client))
        rows = self.cur.fetchall()
        return rows

    def search22(self, no="", item_requested=""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND item_requested = ?", (no, item_requested))
        rows = self.cur.fetchall()
        return rows

    def search222(self, no="",  quote_status =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND  quote_status = ?", (no,  quote_status))
        rows = self.cur.fetchall()
        return rows

    def search2222(self, no="",  offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND  offer_manager = ?", (no,  offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search22222(self, no="",  sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND  sales_manager = ?", (no,  sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search222222(self, no="",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND  cost_meur = ?", (no,  cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search2222222(self, client = "",  item_requested =""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND  item_requested = ?", (client,  item_requested))
        rows = self.cur.fetchall()
        return rows

    def search22222222(self, client = "",  quote_status =""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND  quote_status = ?", (client,  quote_status))
        rows = self.cur.fetchall()
        return rows

    def search222222222(self, client = "",  offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND  offer_manager = ?", (client,  offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search2222222222(self, client = "",  sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND  sales_manager = ?", (client,  sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search22222222222(self, client = "",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND  cost_meur = ?", (client,  cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search222222222222(self, item_requested = "",  quote_status =""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND  quote_status = ?", (item_requested,  quote_status))
        rows = self.cur.fetchall()
        return rows

    def search2222222222222(self, item_requested = "",  offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND  offer_manager = ?", (item_requested,  offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search22222222222222(self, item_requested = "",  sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND  sales_manager = ?", (item_requested,  sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search222222222222222(self, item_requested = "",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND  cost_meur = ?", (item_requested,  cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search2222222222222222(self, quote_status = "",  offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND  offer_manager = ?", (quote_status,  offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search22222222222222222(self, quote_status = "",  sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND  sales_manager = ?", (quote_status,  sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search222222222222222222(self, quote_status = "",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND  cost_meur = ?", (quote_status,  cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search2222222222222222222(self, offer_manager = "",  sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE offer_manager = ? AND  sales_manager = ?", (offer_manager,  sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search22222222222222222222(self, offer_manager = "",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE offer_manager = ? AND  cost_meur = ?", (offer_manager,  cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search222222222222222222222(self, sales_manager = "",  cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE sales_manager = ? AND  cost_meur = ?", (sales_manager,  cost_meur))
        rows = self.cur.fetchall()
        return rows

# 3 fields search:
    def search3(self, no = "", client = "", item_requested =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ?", (no, client, item_requested))
        rows = self.cur.fetchall()
        return rows

    def search33(self, no = "", client = "", quote_status =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND quote_status = ?", (no, client, quote_status))
        rows = self.cur.fetchall()
        return rows

    def search333(self, no = "", client = "", offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND offer_manager = ?", (no, client, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search3333(self, no = "", client = "", sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND sales_manager = ?", (no, client, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search33333(self, no = "", client = "", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND cost_meur = ?", (no, client, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search333333(self, no = "", item_requested = "", quote_status =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND item_requested = ? AND quote_status = ?", (no, item_requested, quote_status))
        rows = self.cur.fetchall()
        return rows

    def search3333333(self, no = "", item_requested = "", offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND item_requested = ? AND offer_manager = ?", (no, item_requested, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search33333333(self, no = "", item_requested = "", sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND item_requested = ? AND sales_manager = ?", (no, item_requested, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333(self, no = "", item_requested = "", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND item_requested = ? AND cost_meur = ?", (no, item_requested, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search3333333333(self, no = "", quote_status = "", offer_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND quote_status = ? AND offer_manager = ?", (no, quote_status, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search33333333333(self, no = "", quote_status = "", sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND quote_status = ? AND sales_manager = ?", (no, quote_status, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333(self, no = "", quote_status = "", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND quote_status = ? AND cost_meur = ?", (no, quote_status, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333(self, no = "", offer_manager = "", sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND offer_manager = ? AND sales_manager = ?", (no, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333(self, no = "", offer_manager = "", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND offer_manager = ? AND cost_meur = ?", (no, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333(self, no="", sales_manager ="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND sales_manager = ? AND cost_meur = ?", (no, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333(self, client="", item_requested ="", quote_status=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ?", (client, item_requested, quote_status))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333333(self, client="", item_requested ="", offer_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND offer_manager = ?", (client, item_requested, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333333(self, client="", item_requested ="", sales_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND sales_manager = ?", (client, item_requested, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333333(self, client="", item_requested ="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND cost_meur = ?", (client, item_requested, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333333333(self, client="", quote_status ="", offer_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND quote_staus = ? AND offer_manager = ?",
                         (client, quote_status, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333333333(self, client="", quote_status ="", sales_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND quote_staus = ? AND sales_manager = ?",
                         (client, quote_status, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333333333(self, client="", quote_status ="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND quote_staus = ? AND cost_meur = ?",
                         (client, quote_status, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333333333333(self, client="", offer_manager ="", sales_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND offer_manager = ? AND sales_manager = ?",
                         (client, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333333333333(self, client="", offer_manager ="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND offer_manager = ? AND cost_meur = ?",
                         (client, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333333333333(self, client="", sales_manager ="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND sales_manager = ? AND cost_meur = ?",
                         (client, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333333333333333(self, item_requested = "", quote_status ="", offer_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND offer_manager = ?",
                         (item_requested, quote_status, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333333333333333(self, item_requested = "", quote_status ="", sales_manager=""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND sales_manager = ?",
                         (item_requested, quote_status, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333333333333333(self, item_requested="", quote_status="", cost_meur=""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND cost_meur = ?",
                         (item_requested, quote_status, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search33333333333333333333333333333(self, quote_status="", offer_manager ="", sales_manager =""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND offer_manager = ? AND sales_manager = ?",
                         (quote_status, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search333333333333333333333333333333(self, quote_status="", offer_manager ="", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND offer_manager = ? AND cost_meur = ?",
                         (quote_status, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search3333333333333333333333333333333(self, offer_manager ="", sales_manager = "", cost_meur =""):
        self.cur.execute("SELECT * FROM entry WHERE offer_manager = ? AND sales_manager = ?, cost_meur = ?",
                         (offer_manager, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

# 4 fields search:
    def search4(self, no = "", client = "", item_requested ="", quote_status = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ?", (no, client, item_requested, quote_status))
        rows = self.cur.fetchall()
        return rows

    def search44(self, no = "", client = "", item_requested ="", offer_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND offer_manager = ?", (no, client, item_requested, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search444(self, no = "", client = "", item_requested ="", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND sales_manager = ?", (no, client, item_requested, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search4444(self, no = "", client = "", item_requested ="", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND cost_meur = ?", (no, client, item_requested, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search44444(self, client = "", item_requested ="", quote_status = "", offer_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ?", (client, item_requested, quote_status, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search444444(self, client = "", item_requested ="", quote_status = "", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND sales_manager = ?", (client, item_requested, quote_status, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search4444444(self, client = "", item_requested ="", quote_status = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND cost_meur = ?", (client, item_requested, quote_status, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search44444444(self, item_requested ="", quote_status = "", offer_manager = "", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND offer_manager = ? AND sales_manager = ?", (item_requested, quote_status, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search444444444(self, item_requested ="", quote_status = "", offer_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND offer_manager = ? AND cost_meur = ?", (item_requested, quote_status, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search4444444444(self, quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE quote_status = ? AND offer_manager = ? AND sales_manager = ?, cost_meur = ?", (quote_status, offer_manager, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

# 5 fields search:
    def search5(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ?", (no, client, item_requested, quote_status, offer_manager))
        rows = self.cur.fetchall()
        return rows

    def search55(self, no = "", client = "", item_requested ="", quote_status = "", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? AND sales_manager = ?", (no, client, item_requested, quote_status, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search555(self, no = "", client = "", item_requested ="", quote_status = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? AND cost_meur = ?", (no, client, item_requested, quote_status, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search5555(self, client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ? AND sales_manager = ?", (client, item_requested, quote_status, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search55555(self, client = "", item_requested ="", quote_status = "", offer_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ? AND cost_meur = ?", (client, item_requested, quote_status, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search555555(self, item_requested ="", quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE item_requested = ? AND quote_status = ? AND offer_manager = ? AND sales_manager = ? AND cost_meur = ?", (item_requested, quote_status, offer_manager, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

# 6 fields search:
    def search6(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ? AND sales_manager = ?", (no, client, item_requested, quote_status, offer_manager, sales_manager))
        rows = self.cur.fetchall()
        return rows

    def search66(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ? AND cost_meur = ?", (no, client, item_requested, quote_status, offer_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def search666(self, client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE client = ? AND item_requested = ? AND quote_status = ? AND offer_manager = ? AND sales_manager = ? AND cost_meur = ?", (client, item_requested, quote_status, offer_manager, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    # 7 fields search:
    def search7(self, no = "", client = "", item_requested ="", quote_status = "", offer_manager = "", sales_manager = "", cost_meur = ""):
        self.cur.execute("SELECT * FROM entry WHERE no = ? AND client = ? AND item_requested = ? AND quote_status = ? "
                         "AND offer_manager = ? AND sales_manager = ? AND cost_meur = ? ",
                         (no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM entry WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur, comments_text):
        self.cur.execute("UPDATE entry SET no = ?, client = ?, item_requested = ?, quote_status = ?, offer_manager = ?, sales_manager = ?, cost_meur = ?, comments = ? WHERE id = ?", (no, client, item_requested, quote_status, offer_manager, sales_manager, cost_meur, comments_text, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    #code for tab 3, data derived from entries:

    def amount_per_client(self,  client = ""):
        self.cur.execute("SELECT cost_meur FROM entry WHERE client = ?", (client,))
        rows = self.cur.fetchall()
        return rows

    def amount_per_item(self,  item_requested = ""):
        self.cur.execute("SELECT cost_meur FROM entry WHERE item_requested = ?", (item_requested,))
        rows = self.cur.fetchall()
        return rows