from app import app, dummy_data, member_store, post_store

if __name__  == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()
