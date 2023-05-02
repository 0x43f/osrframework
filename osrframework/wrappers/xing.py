################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

__author__ = "Felix Brezo, Yaiza Rubio  <contacto@i3visio.com>"
__version__ = "2.0"


from osrframework.utils.platforms import Platform


class Xing(Platform):
    """A <Platform> object for Xing"""
    def __init__(self):
        self.platformName = "Xing"
        self.tags = ["contact", "professional"]

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "https://www.xing.com/profile/" + "<usufy>"
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = ".+"
        #self.validQuery["searchfy"] = ".*"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["Es tut uns leid: Diese Seite ist leider wie vom Winde verweht."]
        #self.notFoundText["searchfy"] = []

        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}

        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""

        # Definition of regular expressions to be searched in usufy mode
        self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "<h2>Contactos de ", "end": "</h2>"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "workLocation\">", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@makes_offer"] = {"start": "\"makesOffer\" itemscope itemtype=\"http://schema.org/Offer\">", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@seeks"] = {"start": "\"seeks\" itemscope itemtype=\"http://schema.org/Demands\">", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@job_title"] = {"start": "<h3 itemprop=\"jobTitle\">", "end": "</h3>"}
        self.fieldsRegExp["usufy"]["@language"] = {"start": "<ul id=\"language-skills\" itemscope itemtype=\"http://schema.org/Language\">", "end": "</ul>"}
        self.fieldsRegExp["usufy"]["@interests"] = {"start": "<div id=\"interests\".*>", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@education"] = {"start": "<li  itemscope itemtype=\"http://schema.org/EducationalOrganization\">", "end": "</li>"}

        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
