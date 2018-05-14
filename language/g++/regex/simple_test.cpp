#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main ()
{
    const char      *ip = "\\b(?:(?:25[0-5]|2[0-4][0-9]"
            "|[01]?[0-9][0-9]?)\\.){3}"
            "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
            "/(?:[1-32])\\b";
    regex ipMatch(ip);

    if (regex_match("127.0.0.1/24", ipMatch)) {
        cout << "string literal matched\n";
    }

    string s ("subject");
    regex e ("(sub)(.*)");
    if (regex_match (s,e))
        cout << "string object matched\n";

    if ( regex_match ( s.begin(), s.end(), e ) )
        cout << "range matched\n";

    cmatch cm;        // same as match_results<const char*> cm;
    regex_match ("subject",cm,e);
    cout << "string literal with " << cm.size() << " matches\n";

    smatch sm;        // same as match_results<string::const_iterator> sm;
    regex_match (s,sm,e);
    cout << "string object with " << sm.size() << " matches\n";

    regex_match ( s.cbegin(), s.cend(), sm, e);
    cout << "range with " << sm.size() << " matches\n";

    // using explicit flags:
    regex_match ( "subject", cm, e, regex_constants::match_default );

    cout << "the matches were: ";
    for (unsigned i=0; i<sm.size(); ++i) {
        cout << "[" << sm[i] << "] ";
    }

    cout << endl;

    return 0;
}
