from flask import Flask, Blueprint, jsonify
from request_mapper import request_json_mapping
from model import Test_Content

# Create Main BluePrint.
main = Blueprint('Main', __name__)


@main.route('/Test', methods=['POST'])
@request_json_mapping(Test_Content)
def Test(test_content: Test_Content):

    return jsonify(f"{test_content.__class__}:{test_content.__dict__}")


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(main)
    app.run()
