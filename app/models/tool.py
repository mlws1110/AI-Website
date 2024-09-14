from app import db

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    features = db.Column(db.String(200))
    pricing = db.Column(db.String(50))
    website = db.Column(db.String(200), nullable=True)  # New field for tool website

    def __repr__(self):
        return f'<Tool {self.name}>'