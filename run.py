"""
User Service

Start the User Service and initializes logging
"""

import os
from service import app

# Pull options from environment
DEBUG = (os.getenv('DEBUG', 'True') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print "******************************************"
    print " U S E R  S E R V I C E   R U N N I N G"
    print "******************************************"
    app.run(host='0.0.0.0', port=int(PORT), debug=DEBUG)
