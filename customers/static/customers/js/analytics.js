(function(){var aa=encodeURIComponent,f=window,ba=setTimeout,n=Math;function Pc(a,b){return a.href=b}function fa(a,b){return a.name=b}
    var Qc = "replace", q = "data", m = "match", xc = "send", ja = "port", u = "createElement", id = "setAttribute", da = "getTime", x = "host", A = "split", B = "location", ra = "hasOwnProperty", ma = "hostname", ga = "search", E = "protocol", Ab = "href", kd = "action", G = "apply", p = "push", h = "hash", s = "test", ha = "slice", r = "cookie", t = "indexOf", ia = "defaultValue", v = "name", y = "length", z = "prototype", la = "clientWidth", jd = "target", C = "call", na = "clientHeight", F = "substring", oa = "navigator", Ub = "parentNode", H = "join", I = "toLowerCase";
    var pa = new function () {
        var a = [];
        this.set = function (b) {
            a[b] = !0
        };
        this.M = function () {
            for (var b = [], c = 0; c < a[y]; c++)a[c] && (b[n.floor(c / 6)] = b[n.floor(c / 6)] ^ 1 << c % 6);
            for (c = 0; c < b[y]; c++)b[c] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(b[c] || 0);
            return b[H]("") + "~"
        }
    };
    function J(a) {
        pa.set(a)
    }
    var ea = function (a) {
        return "function" == typeof a
    }, ka = function (a) {
        return "[object Array]" == Object[z].toString[C](Object(a))
    }, qa = function (a) {
        return void 0 != a && -1 < (a.constructor + "")[t]("String")
    }, D = function (a, b) {
        return 0 == a[t](b)
    }, sa = function (a) {
        return a ? a[Qc](/^[\s\xa0]+|[\s\xa0]+$/g, "") : ""
    }, ta = function (a) {
        var b = M[u]("img");
        b.width = 1;
        b.height = 1;
        b.src = a;
        return b
    }, ua = function () {
    }, K = function (a) {
        if (aa instanceof Function)return aa(a);
        J(28);
        return a
    }, L = function (a, b, c, d) {
        try {
            a.addEventListener ? a.addEventListener(b,
                c,!!d):a.attachEvent&&a.attachEvent("on"+b,c)}catch(e){J(27)}},va=function(a,b,c){a.removeEventListener?a.removeEventListener(b,c,!1):a.detachEvent&&a.detachEvent("on"+b,c)},wa=function(a,b){if(a){var c=M[u]("script");c.type="text/javascript";c.async=!0;c.src=a;b&&(c.id=b);var d=M.getElementsByTagName("script")[0];d[Ub].insertBefore(c,d)}},xa=function(){var a=""+M[B][ma];return 0==a[t]("www.")?a[F](4):a},ya=function(a){var b=M.referrer;if(/^https?:\/\//i[s](b)){if(a)return b;a="//"+M[B][ma];var c=
b[t](a);if(5==c||6==c)if(a=b.charAt(c+a[y]),"/"==a||"?"==a||""==a||":"==a)return;return b}},za=function(a,b){if(1==b[y]&&null!=b[0]&&"object"===typeof b[0])return b[0];for(var c={},d=n.min(a[y]+1,b[y]),e=0;e<d;e++)if("object"===typeof b[e]){for(var g in b[e])b[e][ra](g)&&(c[g]=b[e][g]);break}else e<a[y]&&(c[a[e]]=b[e]);return c};var N=function(){this.keys=[];this.w={};this.m={}};N[z].set=function(a,b,c){this.keys[p](a);c?this.m[":"+a]=b:this.w[":"+a]=b};N[z].get=function(a){return this.m[ra](":"+a)?this.m[":"+a]:this.w[":"+a]};N[z].map=function(a){for(var b=0;b<this.keys[y];b++){var c=this.keys[b],d=this.get(c);d&&a(c,d)}};var O=f,M=document,fb=function(a){ba(a,100)},Mc=function(){for(var a=O[oa].userAgent+(M[r]?M[r]:"")+(M.referrer?M.referrer:""),b=a[y],c=O.history[y];0<c;)a+=c--^b++;return La(a)};var Aa=function(a){var b=O._gaUserPrefs;if(b&&b.ioo&&b.ioo()||a&&!0===O["ga-disable-"+a])return!0;try{var c=O.external;if(c&&c._gaUserPrefs&&"oo"==c._gaUserPrefs)return!0}catch(d){}return!1};var Ca=function(a){var b=[],c=M[r][A](";");a=new RegExp("^\\s*"+a+"=\\s*(.*?)\\s*$");for(var d=0;d<c[y];d++){var e=c[d][m](a);e&&b[p](e[1])}return b},zc=function(a,b,c,d,e,g){e=Aa(e)?!1:eb[s](M[B][ma])||"/"==c&&vc[s](d)?!1:!0;if(!e)return!1;b&&1200<b[y]&&(b=b[F](0,1200),J(24));c=a+"="+b+"; path="+c+"; ";g&&(c+="expires="+(new Date((new Date)[da]()+g)).toGMTString()+"; ");d&&"none"!=d&&(c+="domain="+d+";");d=M[r];M.cookie=c;if(!(d=d!=M[r]))t:{a=Ca(a);for(d=0;d<a[y];d++)if(b==a[d]){d=!0;break t}d=!1}return d},
Cc=function(a){return K(a)[Qc](/\(/g,"%28")[Qc](/\)/g,"%29")},vc=/^(www\.)?google(\.com?)?(\.[a-z]{2})?$/,eb=/(^|\.)doubleclick\.net$/i;var oc=function(){return(Ba||"https:"==M[B][E]?"https:":"http:")+"//www.google-analytics.com"},Da=function(a){fa(this,"len");this.message=a+"-8192"},Ea=function(a){fa(this,"ff2post");this.message=a+"-2036"},Ga=function(a,b,c,d){c=c||ua;d&&(d=c,O[oa].sendBeacon?O[oa].sendBeacon(a,b)?(d(),d=!0):d=!1:d=!1);if(!d)if(2036>=b[y])wc(a,b,c);else if(8192>=b[y]){if(0<=O[oa].userAgent[t]("Firefox")&&![].reduce)throw new Ea(b[y]);wd(a,b,c)||xd(a,b,c)||Fa(b,c)||c()}else throw new Da(b[y]);},wc=function(a,b,c){var d=
ta(a+"?"+b);d.onload=d.onerror=function(){d.onload=null;d.onerror=null;c()}},xd=function(a,b,c){var d;d=O.XDomainRequest;if(!d)return!1;d=new d;d.open("POST",a);d.onerror=function(){c()};d.onload=c;d[xc](b);return!0},wd=function(a,b,c){var d=O.XMLHttpRequest;if(!d)return!1;var e=new d;if(!("withCredentials"in e))return!1;e.open("POST",a,!0);e.withCredentials=!0;e.setRequestHeader("Content-Type","text/plain");e.onreadystatechange=function(){4==e.readyState&&(c(),e=null)};e[xc](b);return!0},Fa=function(a,
b){if(!M.body)return fb(function(){Fa(a,b)}),!0;a=aa(a);try{var c=M[u]('<iframe name="'+a+'"></iframe>')}catch(d){c=M[u]("iframe"),fa(c,a)}c.height="0";c.width="0";c.style.display="none";c.style.visibility="hidden";var e=M[B],e=oc()+"/analytics_iframe.html#"+aa(e[E]+"//"+e[x]+"/favicon.ico"),g=function(){c.src="";c[Ub]&&c[Ub].removeChild(c)};L(O,"beforeunload",g);var ca=!1,l=0,k=function(){if(!ca){try{if(9<l||c.contentWindow[B][x]==M[B][x]){ca=!0;g();va(O,"beforeunload",g);b();return}}catch(a){}l++;
ba(k,200)}};L(c,"load",k);M.body.appendChild(c);c.src=e;return!0};var Ha=function(){this.t=[]};Ha[z].add=function(a){this.t[p](a)};Ha[z].D=function(a){try{for(var b=0;b<this.t[y];b++){var c=a.get(this.t[b]);c&&ea(c)&&c[C](O,a)}}catch(d){}b=a.get(Ia);b!=ua&&ea(b)&&(a.set(Ia,ua,!0),ba(b,10))};function Ja(a){if(100!=a.get(Ka)&&La(P(a,Q))%1E4>=100*R(a,Ka))throw"abort";}function Ma(a){if(Aa(P(a,Na)))throw"abort";}function Oa(){var a=M[B][E];if("http:"!=a&&"https:"!=a)throw"abort";}
function Pa(a){try{O.XMLHttpRequest&&"withCredentials"in new O.XMLHttpRequest?J(40):O.XDomainRequest&&J(41),O[oa].sendBeacon&&J(42)}catch(b){}a.set(Ac,R(a,Ac)+1);var c=[];Qa.map(function(b,e){if(e.p){var g=a.get(b);void 0!=g&&g!=e[ia]&&("boolean"==typeof g&&(g*=1),c[p](e.p+"="+K(""+g)))}});c[p]("z="+Bd());a.set(Ra,c[H]("&"),!0)}function Sa(a){var b=P(a,gd)||oc()+"/collect";Ga(b,P(a,Ra),a.get(Ia),a.get(Vd));a.set(Ia,ua,!0)}
    function Hc(a) {
        var b = O.gaData;
        b && (b.expId && a.set(Nc, b.expId), b.expVar && a.set(Oc, b.expVar))
    }
    function cd() {
        if (O[oa] && "preview" == O[oa].loadPurpose)throw"abort";
    }
    function yd(a) {
        var b = O.gaDevIds;
        ka(b) && 0 != b[y] && a.set("&did", b[H](","), !0)
    }
    function vb(a) {
        if (!a.get(Na))throw"abort";
    }
    var hd = function () {
        return n.round(2147483647 * n.random())
    }, Bd = function () {
        try {
            var a = new Uint32Array(1);
            O.crypto.getRandomValues(a);
            return a[0] & 2147483647
        } catch (b) {
            return hd()
        }
    };
    function Ta(a) {
        var b = R(a, Ua);
        500 <= b && J(15);
        var c = P(a, Va);
        if ("transaction" != c && "item" != c) {
            var c = R(a, Wa), d = (new Date)[da](), e = R(a, Xa);
            0 == e && a.set(Xa, d);
            e = n.round(2 * (d - e) / 1E3);
            0 < e && (c = n.min(c + e, 20), a.set(Xa, d));
            if (0 >= c)throw"abort";
            a.set(Wa, --c)
        }
        a.set(Ua, ++b)
    }
    var Ya = function () {
        this.data = new N
    }, Qa = new N, Za = [];
    Ya[z].get = function (a) {
        var b = $a(a), c = this[q].get(a);
        b && void 0 == c && (c = ea(b[ia]) ? b[ia]() : b[ia]);
        return b && b.n ? b.n(this, a, c) : c
    };
    var P = function (a, b) {
        var c = a.get(b);
        return void 0 == c ? "" : "" + c
    }, R = function (a, b) {
        var c = a.get(b);
        return void 0 == c || "" === c ? 0 : 1 * c
    };
    Ya[z].set = function (a, b, c) {
        if (a)if ("object" == typeof a)for (var d in a)a[ra](d) && ab(this, d, a[d], c); else ab(this, a, b, c)
    };
    var ab=function(a,b,c,d){if(void 0!=c)switch(b){case Na:wb[s](c)}var e=$a(b);e&&e.o?e.o(a,b,c,d):a[q].set(b,c,d)},bb=function(a,b,c,d,e){fa(this,a);this.p=b;this.n=d;this.o=e;this.defaultValue=c},$a=function(a){var b=Qa.get(a);if(!b)for(var c=0;c<Za[y];c++){var d=Za[c],e=d[0].exec(a);if(e){b=d[1](e);Qa.set(b[v],b);break}}return b},yc=function(a){var b;Qa.map(function(c,d){d.p==a&&(b=d)});return b&&b[v]},S=function(a,b,c,d,e){a=new bb(a,b,c,d,e);Qa.set(a[v],a);return a[v]},cb=function(a,b){Za[p]([new RegExp("^"+
a+"$"),b])},T=function(a,b,c){return S(a,b,c,void 0,db)},db=function(){};var gb=qa(f.GoogleAnalyticsObject)&&sa(f.GoogleAnalyticsObject)||"ga",Ba=!1,hb=T("apiVersion","v"),ib=T("clientVersion","_v");S("anonymizeIp","aip");var jb=S("adSenseId","a"),Va=S("hitType","t"),Ia=S("hitCallback"),Ra=S("hitPayload");S("nonInteraction","ni");S("currencyCode","cu");var Vd=S("useBeacon",void 0,!1);S("dataSource","ds");S("sessionControl","sc","");S("sessionGroup","sg");S("queueTime","qt");var Ac=S("_s","_s");S("screenName","cd");
var kb=S("location","dl",""),lb=S("referrer","dr"),mb=S("page","dp","");S("hostname","dh");var nb=S("language","ul"),ob=S("encoding","de");S("title","dt",function(){return M.title||void 0});cb("contentGroup([0-9]+)",function(a){return new bb(a[0],"cg"+a[1])});var pb=S("screenColors","sd"),qb=S("screenResolution","sr"),rb=S("viewportSize","vp"),sb=S("javaEnabled","je"),tb=S("flashVersion","fl");S("campaignId","ci");S("campaignName","cn");S("campaignSource","cs");S("campaignMedium","cm");
S("campaignKeyword","ck");S("campaignContent","cc");var ub=S("eventCategory","ec"),xb=S("eventAction","ea"),yb=S("eventLabel","el"),zb=S("eventValue","ev"),Bb=S("socialNetwork","sn"),Cb=S("socialAction","sa"),Db=S("socialTarget","st"),Eb=S("l1","plt"),Fb=S("l2","pdt"),Gb=S("l3","dns"),Hb=S("l4","rrt"),Ib=S("l5","srt"),Jb=S("l6","tcp"),Kb=S("l7","dit"),Lb=S("l8","clt"),Mb=S("timingCategory","utc"),Nb=S("timingVar","utv"),Ob=S("timingLabel","utl"),Pb=S("timingValue","utt");S("appName","an");
S("appVersion","av","");S("appId","aid","");S("appInstallerId","aiid","");S("exDescription","exd");S("exFatal","exf");var Nc=S("expId","xid"),Oc=S("expVar","xvar"),Rc=S("_utma","_utma"),Sc=S("_utmz","_utmz"),Tc=S("_utmht","_utmht"),Ua=S("_hc",void 0,0),Xa=S("_ti",void 0,0),Wa=S("_to",void 0,20);cb("dimension([0-9]+)",function(a){return new bb(a[0],"cd"+a[1])});cb("metric([0-9]+)",function(a){return new bb(a[0],"cm"+a[1])});S("linkerParam",void 0,void 0,Bc,db);
var ld=S("usage","_u",void 0,function(){return pa.M()},db);S("forceSSL",void 0,void 0,function(){return Ba},function(a,b,c){J(34);Ba=!!c});var ed=S("_j1","jid"),Hd=S("_j2","gjid");cb("\\&(.*)",function(a){var b=new bb(a[0],a[1]),c=yc(a[0][F](1));c&&(b.n=function(a){return a.get(c)},b.o=function(a,b,g,ca){a.set(c,g,ca)},b.p=void 0);return b});
var Qb=T("_oot"),dd=S("previewTask"),Rb=S("checkProtocolTask"),md=S("validationTask"),Sb=S("checkStorageTask"),Uc=S("historyImportTask"),Tb=S("samplerTask"),Vb=T("_rlt"),Wb=S("buildHitTask"),Xb=S("sendHitTask"),Vc=S("ceTask"),zd=S("devIdTask"),Cd=S("timingTask"),Ld=S("displayFeaturesTask"),V=T("name"),Q=T("clientId","cid"),Ad=S("userId","uid"),Na=T("trackingId","tid"),U=T("cookieName",void 0,"_ga"),W=T("cookieDomain"),Yb=T("cookiePath",void 0,"/"),Zb=T("cookieExpires",void 0,63072E3),$b=T("legacyCookieDomain"),
Wc=T("legacyHistoryImport",void 0,!0),ac=T("storage",void 0,"cookie"),bc=T("allowLinker",void 0,!1),cc=T("allowAnchor",void 0,!0),Ka=T("sampleRate","sf",100),dc=T("siteSpeedSampleRate",void 0,1),ec=T("alwaysSendReferrer",void 0,!1),gd=S("transportUrl"),Md=S("_r","_r");
    function X(a, b, c, d) {
        b[a] = function () {
            try {
                return d && J(d), c[G](this, arguments)
            } catch (b) {
                var g = b && b[v];
                if (!(1 <= 100 * n.random() || Aa("?"))) {
                    var ca = ["t=error", "_e=exc", "_v=j31", "sr=1"];
                    a && ca[p]("_f=" + a);
                    g && ca[p]("_m=" + K(g[F](0, 100)));
                    ca[p]("aip=1");
                    ca[p]("z=" + hd());
                    Ga(oc() + "/collect", ca[H]("&"))
                }
                throw b;
            }
        }
    }
    var Od = function () {
        this.V = 1E4;
        this.fa = void 0;
        this.$ = !1;
        this.ea = 1
    }, Ed = function () {
        var a = new Od, b;
        if (a.fa && a.$)return 0;
        a.$ = !0;
        if (0 == a.V)return 0;
        void 0 === b && (b = Bd());
        return 0 == b % a.V ? n.floor(b / a.V) % a.ea + 1 : 0
    };
    function fc() {
        var a, b, c;
        if ((c = (c = O[oa]) ? c.plugins : null) && c[y])for (var d = 0; d < c[y] && !b; d++) {
            var e = c[d];
            -1 < e[v][t]("Shockwave Flash") && (b = e.description)
        }
        if (!b)try {
            a = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7"), b = a.GetVariable("$version")
        } catch (g) {
        }
        if (!b)try {
            a = new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6"), b = "WIN 6,0,21,0", a.AllowScriptAccess = "always", b = a.GetVariable("$version")
        } catch (ca) {
        }
        if (!b)try {
            a = new ActiveXObject("ShockwaveFlash.ShockwaveFlash"), b = a.GetVariable("$version")
        } catch (l) {
        }
        b &&
        (a = b[m](/[\d]+/g)) && 3 <= a[y] && (b = a[0] + "." + a[1] + " r" + a[2]);
        return b || void 0
    }
    var gc = function (a, b) {
        var c = n.min(R(a, dc), 100);
        if (!(La(P(a, Q)) % 100 >= c) && (c = {}, Ec(c) || Fc(c))) {
            var d = c[Eb];
            void 0 == d || Infinity == d || isNaN(d) || (0 < d ? (Y(c, Gb), Y(c, Jb), Y(c, Ib), Y(c, Fb), Y(c, Hb), Y(c, Kb), Y(c, Lb), b(c)) : L(O, "load", function () {
                gc(a, b)
            }, !1))
        }
    }, Ec = function (a) {
        var b = O.performance || O.webkitPerformance, b = b && b.timing;
        if (!b)return !1;
        var c = b.navigationStart;
        if (0 == c)return !1;
        a[Eb] = b.loadEventStart - c;
        a[Gb] = b.domainLookupEnd - b.domainLookupStart;
        a[Jb] = b.connectEnd - b.connectStart;
        a[Ib] = b.responseStart - b.requestStart;
        a[Fb]=b.responseEnd-b.responseStart;a[Hb]=b.fetchStart-c;a[Kb]=b.domInteractive-c;a[Lb]=b.domContentLoadedEventStart-c;return!0},Fc=function(a){if(O.top!=O)return!1;var b=O.external,c=b&&b.onloadT;b&&!b.isValidLoadTime&&(c=void 0);2147483648<c&&(c=void 0);0<c&&b.setPageReadyTime();if(void 0==c)return!1;a[Eb]=c;return!0},Y=function(a,b){var c=a[b];if(isNaN(c)||Infinity==c||0>c)a[b]=void 0},Fd=function(a){return function(b){"pageview"!=b.get(Va)||a.I||(a.I=!0,gc(b,function(b){a[xc]("timing",b)}))}};var hc=!1,mc=function(a){if("cookie"==P(a,ac)){var b=P(a,U),c=nd(a),d=kc(P(a,Yb)),e=lc(P(a,W)),g=1E3*R(a,Zb),ca=P(a,Na);if("auto"!=e)zc(b,c,d,e,ca,g)&&(hc=!0);else{J(32);var l;t:{c=[];e=xa()[A](".");if(4==e[y]&&(l=e[e[y]-1],parseInt(l,10)==l)){l=["none"];break t}for(l=e[y]-2;0<=l;l--)c[p](e[ha](l)[H]("."));c[p]("none");l=c}for(var k=0;k<l[y];k++)if(e=l[k],a[q].set(W,e),c=nd(a),zc(b,c,d,e,ca,g)){hc=!0;return}a[q].set(W,"auto")}}},nc=function(a){if("cookie"==P(a,ac)&&!hc&&(mc(a),!hc))throw"abort";},
Yc=function(a){if(a.get(Wc)){var b=P(a,W),c=P(a,$b)||xa(),d=Xc("__utma",c,b);d&&(J(19),a.set(Tc,(new Date)[da](),!0),a.set(Rc,d.R),(b=Xc("__utmz",c,b))&&d[h]==b[h]&&a.set(Sc,b.R))}},nd=function(a){var b=Cc(P(a,Q)),c=ic(P(a,W));a=jc(P(a,Yb));1<a&&(c+="-"+a);return["GA1",c,b][H](".")},Gc=function(a,b,c){for(var d=[],e=[],g,ca=0;ca<a[y];ca++){var l=a[ca];if(l.r[c]==b)d[p](l);else void 0==g||l.r[c]<g?(e=[l],g=l.r[c]):l.r[c]==g&&e[p](l)}return 0<d[y]?d:e},lc=function(a){return 0==a[t](".")?a.substr(1):
            a
        }, ic = function (a) {
            return lc(a)[A](".")[y]
        }, kc = function (a) {
            if (!a)return "/";
            1 < a[y] && a.lastIndexOf("/") == a[y] - 1 && (a = a.substr(0, a[y] - 1));
            0 != a[t]("/") && (a = "/" + a);
            return a
        }, jc = function (a) {
            a = kc(a);
            return "/" == a ? 1 : a[A]("/")[y]
        };
    function Xc(a, b, c) {
        "none" == b && (b = "");
        var d = [], e = Ca(a);
        a = "__utma" == a ? 6 : 2;
        for (var g = 0; g < e[y]; g++) {
            var ca = ("" + e[g])[A](".");
            ca[y] >= a && d[p]({hash: ca[0], R: e[g], O: ca})
        }
        return 0 == d[y] ? void 0 : 1 == d[y] ? d[0] : Zc(b, d) || Zc(c, d) || Zc(null, d) || d[0]
    }
    function Zc(a, b) {
        var c, d;
        null == a ? c = d = 1 : (c = La(a), d = La(D(a, ".") ? a[F](1) : "." + a));
        for (var e = 0; e < b[y]; e++)if (b[e][h] == c || b[e][h] == d)return b[e]
    }
    var od = new RegExp(/^https?:\/\/([^\/:]+)/), pd = /(.*)([?&#])(?:_ga=[^&#]*)(?:&?)(.*)/;
    function Bc(a) {
        a = a.get(Q);
        var b = Ic(a, 0);
        return "_ga=1." + K(b + "." + a)
    }
    function Ic(a, b) {
        for (var c = new Date, d = O[oa], e = d.plugins || [], c = [a, d.userAgent, c.getTimezoneOffset(), c.getYear(), c.getDate(), c.getHours(), c.getMinutes() + b], d = 0; d < e[y]; ++d)c[p](e[d].description);
        return La(c[H]("."))
    }
    var Dc = function (a) {
        J(48);
        this.target = a;
        this.T = !1
    };
    Dc[z].Q=function(a,b){if(a.tagName){if("a"==a.tagName[I]()){a[Ab]&&Pc(a,qd(this,a[Ab],b));return}if("form"==a.tagName[I]())return rd(this,a)}if("string"==typeof a)return qd(this,a,b)};
var qd=function(a,b,c){var d=pd.exec(b);d&&3<=d[y]&&(b=d[1]+(d[3]?d[2]+d[3]:""));a=a[jd].get("linkerParam");var e=b[t]("?"),d=b[t]("#");c?b+=(-1==d?"#":"&")+a:(c=-1==e?"?":"&",b=-1==d?b+(c+a):b[F](0,d)+c+a+b[F](d));return b},rd=function(a,b){if(b&&b[kd]){var c=a[jd].get("linkerParam")[A]("=")[1];if("get"==b.method[I]()){for(var d=b.childNodes||[],e=0;e<d[y];e++)if("_ga"==d[e][v]){d[e][id]("value",c);return}d=M[u]("input");d[id]("type","hidden");d[id]("name","_ga");d[id]("value",c);b.appendChild(d)}else"post"==
b.method[I]()&&(b.action=qd(a,b[kd]))}};
Dc[z].S=function(a,b,c){function d(c){try{c=c||O.event;var d;t:{var g=c[jd]||c.srcElement;for(c=100;g&&0<c;){if(g[Ab]&&g.nodeName[m](/^a(?:rea)?$/i)){d=g;break t}g=g[Ub];c--}d={}}("http:"==d[E]||"https:"==d[E])&&sd(a,d[ma]||"")&&d[Ab]&&Pc(d,qd(e,d[Ab],b))}catch(w){J(26)}}var e=this;this.T||(this.T=!0,L(M,"mousedown",d,!1),L(M,"touchstart",d,!1),L(M,"keyup",d,!1));if(c){c=function(b){b=b||O.event;if((b=b[jd]||b.srcElement)&&b[kd]){var c=b[kd][m](od);c&&sd(a,c[1])&&rd(e,b)}};for(var g=0;g<M.forms[y];g++)L(M.forms[g],
    "submit", c)
}
};
    function sd(a, b) {
        if (b == M[B][ma])return !1;
        for (var c = 0; c < a[y]; c++)if (a[c]instanceof RegExp) {
            if (a[c][s](b))return !0
        } else if (0 <= b[t](a[c]))return !0;
        return !1
    }
    var Jd = function (a, b, c, d) {
        this.U = b;
        this.aa = c;
        (b = d) || (b = (b = P(a, V)) && "t0" != b ? Wd[s](b) ? "_gat_" + Cc(P(a, Na)) : "_gat_" + Cc(b) : "_gat");
        this.Y = b
    }, Rd = function (a, b) {
        var c = b.get(Wb);
        b.set(Wb, function (b) {
            Pd(a, b);
            var d = c(b);
            Qd(a, b);
            return d
        });
        var d = b.get(Xb);
        b.set(Xb, function (b) {
            var c = d(b);
            Id(a, b);
            return c
        })
    }, Pd = function (a, b) {
        b.get(a.U) || ("1" == Ca(a.Y)[0] ? b.set(a.U, "", !0) : b.set(a.U, "" + hd(), !0))
    }, Qd = function (a, b) {
        b.get(a.U) && zc(a.Y, "1", b.get(Yb), b.get(W), b.get(Na), 6E5)
    }, Id = function (a, b) {
        if (b.get(a.U)) {
            var c = new N,
                d=function(a){c.set($a(a).p,b.get(a))};d(hb);d(ib);d(Na);d(Q);d(a.U);d(ld);var e=a.aa;c.map(function(a,b){e+=K(a)+"=";e+=K(""+b)+"&"});e+="z="+hd();ta(e);b.set(a.U,"",!0)}},Wd=/^gtm\d+$/;var fd=function(a,b){var c=a.b;if(!c.get("dcLoaded")){J(29);O._gaq&&J(52);b=b||{};var d;b[U]&&(d=Cc(b[U]));d=new Jd(c,ed,"https://stats.g.doubleclick.net/collect?t=dc&aip=1&",d);Rd(d,c);c.set("dcLoaded",!0)}};var Sd=function(a){var b;b=a.get("dcLoaded")?!1:"cookie"!=a.get(ac)?!1:!0;b&&(J(51),b=new Jd(a,ed),Pd(b,a),Qd(b,a),a.get(b.U)&&(a.set(Md,1,!0),a.set(gd,oc()+"/r/collect",!0)))};var Kd=function(a,b){var c=a.b;if(!c.get("_rlsaLoaded")){J(38);b=b||{};if(b[U])var d=Cc(b[U]);d=new Jd(c,Hd,"https://www.google.com/ads/ga-audiences?t=sr&aip=1&",d);Rd(d,c);c.set("_rlsaLoaded",!0);tc("displayfeatures",a,b)}};var Lc=function(){var a=O.gaGlobal=O.gaGlobal||{};return a.hid=a.hid||hd()};var ad,bd=function(a,b,c){if(!ad){var d;d=M[B][h];var e=O[v],g=/^#?gaso=([^&]*)/;if(e=(d=(d=d&&d[m](g)||e&&e[m](g))?d[1]:Ca("GASO")[0]||"")&&d[m](/^(?:!([-0-9a-z.]{1,40})!)?([-.\w]{10,1200})$/i))zc("GASO",""+d,c,b,a,0),f._udo||(f._udo=b),f._utcp||(f._utcp=c),a=e[1],wa("https://www.google.com/analytics/web/inpage/pub/inpage.js?"+(a?"prefix="+a+"&":"")+hd(),"_gasojs");ad=!0}};var wb=/^(UA|YT|MO|GP)-(\d+)-(\d+)$/,pc=function(a){function b(a,b){d.b[q].set(a,b)}function c(a,c){b(a,c);d.filters.add(a)}var d=this;this.b=new Ya;this.filters=new Ha;b(V,a[V]);b(Na,sa(a[Na]));b(U,a[U]);b(W,a[W]||xa());b(Yb,a[Yb]);b(Zb,a[Zb]);b($b,a[$b]);b(Wc,a[Wc]);b(bc,a[bc]);b(cc,a[cc]);b(Ka,a[Ka]);b(dc,a[dc]);b(ec,a[ec]);b(ac,a[ac]);b(Ad,a[Ad]);b(hb,1);b(ib,"j31");c(Qb,Ma);c(dd,cd);c(Rb,Oa);c(md,vb);c(Sb,nc);c(Uc,Yc);c(Tb,Ja);c(Vb,Ta);c(Vc,Hc);c(zd,yd);c(Ld,Sd);c(Wb,Pa);c(Xb,Sa);c(Cd,Fd(this));
Jc(this.b,a[Q]);Kc(this.b);this.b.set(jb,Lc());bd(this.b.get(Na),this.b.get(W),this.b.get(Yb))},Jc=function(a,b){if("cookie"==P(a,ac)){hc=!1;var c;i:{var d=Ca(P(a,U));if(d&&!(1>d[y])){c=[];for(var e=0;e<d[y];e++){var g;g=d[e][A](".");var ca=g.shift();("GA1"==ca||"1"==ca)&&1<g[y]?(ca=g.shift()[A]("-"),1==ca[y]&&(ca[1]="1"),ca[0]*=1,ca[1]*=1,g={r:ca,s:g[H](".")}):g=void 0;g&&c[p](g)}if(1==c[y]){J(13);c=c[0].s;break i}if(0==c[y])J(12);else{J(14);d=ic(P(a,W));c=Gc(c,d,0);if(1==c[y]){c=c[0].s;break i}d=
jc(P(a,Yb));c=Gc(c,d,1);c=c[0]&&c[0].s;break i}}c=void 0}c||(c=P(a,W),d=P(a,$b)||xa(),c=Xc("__utma",d,c),(c=void 0==c?void 0:c.O[1]+"."+c.O[2])&&J(10));c&&(a[q].set(Q,c),hc=!0)}c=a.get(cc);if(e=(c=M[B][c?"href":"search"][m]("(?:&|#|\\?)"+K("_ga")[Qc](/([.*+?^=!:${}()|\[\]\/\\])/g,"\\$1")+"=([^&#]*)"))&&2==c[y]?c[1]:"")a.get(bc)?(c=e[t]("."),-1==c?J(22):(d=e[F](c+1),"1"!=e[F](0,c)?J(22):(c=d[t]("."),-1==c?J(22):(e=d[F](0,c),c=d[F](c+1),e!=Ic(c,0)&&e!=Ic(c,-1)&&e!=Ic(c,-2)?J(23):(J(11),a[q].set(Q,c)))))):
J(21);b&&(J(9),a[q].set(Q,K(b)));a.get(Q)||((c=(c=O.gaGlobal&&O.gaGlobal.vid)&&-1!=c[ga](/^(?:utma\.)?\d+\.\d+$/)?c:void 0)?(J(17),a[q].set(Q,c)):(J(8),a[q].set(Q,[hd()^Mc()&2147483647,n.round((new Date)[da]()/1E3)][H]("."))));mc(a)},Kc=function(a){var b=O[oa],c=O.screen,d=M[B];a.set(lb,ya(a.get(ec)));if(d){var e=d.pathname||"";"/"!=e.charAt(0)&&(J(31),e="/"+e);a.set(kb,d[E]+"//"+d[ma]+e+d[ga])}c&&a.set(qb,c.width+"x"+c.height);c&&a.set(pb,c.colorDepth+"-bit");var c=M.documentElement,g=(e=M.body)&&
e[la]&&e[na],ca=[];c&&c[la]&&c[na]&&("CSS1Compat"===M.compatMode||!g)?ca=[c[la],c[na]]:g&&(ca=[e[la],e[na]]);c=0>=ca[0]||0>=ca[1]?"":ca[H]("x");a.set(rb,c);a.set(tb,fc());a.set(ob,M.characterSet||M.charset);a.set(sb,b&&"function"===typeof b.javaEnabled&&b.javaEnabled()||!1);a.set(nb,(b&&(b.language||b.browserLanguage)||"")[I]());if(d&&a.get(cc)&&(b=M[B][h])){b=b[A](/[?&#]+/);d=[];for(c=0;c<b[y];++c)(D(b[c],"utm_id")||D(b[c],"utm_campaign")||D(b[c],"utm_source")||D(b[c],"utm_medium")||D(b[c],"utm_term")||
D(b[c],"utm_content")||D(b[c],"gclid")||D(b[c],"dclid")||D(b[c],"gclsrc"))&&d[p](b[c]);0<d[y]&&(b="#"+d[H]("&"),a.set(kb,a.get(kb)+b))}};pc[z].get=function(a){return this.b.get(a)};pc[z].set=function(a,b){this.b.set(a,b)};var qc={pageview:[mb],event:[ub,xb,yb,zb],social:[Bb,Cb,Db],timing:[Mb,Nb,Pb,Ob]};
pc[z].send=function(a){if(!(1>arguments[y])){var b,c;"string"===typeof arguments[0]?(b=arguments[0],c=[][ha][C](arguments,1)):(b=arguments[0]&&arguments[0][Va],c=arguments);b&&(c=za(qc[b]||[],c),c[Va]=b,this.b.set(c,void 0,!0),this.filters.D(this.b),this.b[q].m={},J(44))}};var rc=function(a){if("prerender"==M.visibilityState)return!1;a();return!0};var td=/^(?:(\w+)\.)?(?:(\w+):)?(\w+)$/,sc=function(a){if(ea(a[0]))this.u=a[0];else{var b=td.exec(a[0]);null!=b&&4==b[y]&&(this.c=b[1]||"t0",this.e=b[2]||"",this.d=b[3],this.a=[][ha][C](a,1),this.e||(this.A="create"==this.d,this.i="require"==this.d,this.g="provide"==this.d,this.ba="remove"==this.d),this.i&&(3<=this.a[y]?(this.X=this.a[1],this.W=this.a[2]):this.a[1]&&(qa(this.a[1])?this.X=this.a[1]:this.W=this.a[1])));b=a[1];a=a[2];if(!this.d)throw"abort";if(this.i&&(!qa(b)||""==b))throw"abort";if(this.g&&
        (!qa(b) || "" == b || !ea(a)))throw"abort";
        if (ud(this.c) || ud(this.e))throw"abort";
        if (this.g && "t0" != this.c)throw"abort";
    }
    };
    function ud(a) {
        return 0 <= a[t](".") || 0 <= a[t](":")
    }
    var Yd, Zd, $d;
    Yd = new N;
    $d = new N;
    Zd = {ec: 45, ecommerce: 46, linkid: 47};
    var tc=function(a,b,c){b==$?J(35):b.get(V);var d=Yd.get(a);if(!ea(d))return!1;b.plugins_=b.plugins_||new N;if(b.plugins_.get(a))return!0;b.plugins_.set(a,new d(b,c||{}));return!0},ae=function(a){function b(a){var b=(a[ma]||"")[A](":")[0][I](),c=(a[E]||"")[I](),c=1*a[ja]||("http:"==c?80:"https:"==c?443:"");a=a.pathname||"";D(a,"/")||(a="/"+a);return[b,""+c,a]}var c=M[u]("a");Pc(c,M[B][Ab]);var d=(c[E]||"")[I](),e=b(c),g=c[ga]||"",ca=d+"//"+e[0]+(e[1]?":"+e[1]:"");D(a,"//")?a=d+a:D(a,"/")?a=ca+a:!a||
D(a,"?")?a=ca+e[2]+(a||g):0>a[A]("/")[0][t](":")&&(a=ca+e[2][F](0,e[2].lastIndexOf("/"))+"/"+a);Pc(c,a);d=b(c);return{protocol:(c[E]||"")[I](),host:d[0],port:d[1],path:d[2],G:c[ga]||"",url:a||""}};var Z={ga:function(){Z.f=[]}};Z.ga();Z.D=function(a){var b=Z.J[G](Z,arguments),b=Z.f.concat(b);for(Z.f=[];0<b[y]&&!Z.v(b[0])&&!(b.shift(),0<Z.f[y]););Z.f=Z.f.concat(b)};
Z.J=function(a){for(var b=[],c=0;c<arguments[y];c++)try{var d=new sc(arguments[c]);if(d.g)Yd.set(d.a[0],d.a[1]);else{if(d.i){var e=d,g=e.a[0];if(!ea(Yd.get(g))&&!$d.get(g)){Zd[ra](g)&&J(Zd[g]);var ca=e.X;!ca&&Zd[ra](g)?(J(39),ca=g+".js"):J(43);if(ca){ca&&0<=ca[t]("/")||(ca=(Ba||"https:"==M[B][E]?"https:":"http:")+"//www.google-analytics.com/plugins/ua/"+ca);var l=ae(ca),e=void 0;var k=l[E],w=M[B][E],e="https:"==k||k==w?!0:"http:"!=k?!1:"http:"==w;var Xd;if(Xd=e){var e=l,be=ae(M[B][Ab]);if(e.G||0<=
e.url[t]("?")||0<=e.path[t]("://"))Xd=!1;else if(e[x]==be[x]&&e[ja]==be[ja])Xd=!0;else{var ce="http:"==e[E]?80:443;Xd="www.google-analytics.com"==e[x]&&(e[ja]||ce)==ce&&D(e.path,"/plugins/")?!0:!1}}Xd&&(wa(l.url),$d.set(g,!0))}}}b[p](d)}}catch(de){}return b};
Z.v=function(a){try{if(a.u)a.u[C](O,$.j("t0"));else{var b=a.c==gb?$:$.j(a.c);if(a.A)"t0"==a.c&&$.create[G]($,a.a);else if(a.ba)$.remove(a.c);else if(b)if(a.i){if(!tc(a.a[0],b,a.W))return!0}else if(a.e){var c=a.d,d=a.a,e=b.plugins_.get(a.e);e[c][G](e,d)}else b[a.d][G](b,a.a)}}catch(g){}};var $=function(a){J(1);Z.D[G](Z,[arguments])};$.h={};$.P=[];$.L=0;$.answer=42;var uc=[Na,W,V];$.create=function(a){var b=za(uc,[][ha][C](arguments));b[V]||(b[V]="t0");var c=""+b[V];if($.h[c])return $.h[c];b=new pc(b);$.h[c]=b;$.P[p](b);return b};$.remove=function(a){for(var b=0;b<$.P[y];b++)if($.P[b].get(V)==a){$.P.splice(b,1);$.h[a]=null;break}};$.j=function(a){return $.h[a]};$.K=function(){return $.P[ha](0)};
$.N=function(){"ga"!=gb&&J(49);var a=O[gb];if(!a||42!=a.answer){$.L=a&&a.l;$.loaded=!0;var b=O[gb]=$;X("create",b,b.create,3);X("remove",b,b.remove);X("getByName",b,b.j,5);X("getAll",b,b.K,6);b=pc[z];X("get",b,b.get,7);X("set",b,b.set,4);X("send",b,b[xc],2);b=Ya[z];X("get",b,b.get);X("set",b,b.set);for (var b = M.getElementsByTagName("script"), c = 0; c < b[y] && 100 > c; c++) {
    var d;
    d = (d = b[c].src) ? 0 != d[t]("https://www.google-analytics.com/analytics") ? !1 : !0 : !1;
    if (d) {
        J(33);
        break;
    }
}"https:"!=M[B][E]&&!Ba&&Ed()&&
(J(36), Ba = !0);
    (O.gaplugins = O.gaplugins || {}).Linker = Dc;
    b = Dc[z];
    Yd.set("linker", Dc);
    X("decorate", b, b.Q, 20);
    X("autoLink", b, b.S, 25);
    Yd.set("displayfeatures", fd);
    Yd.set("adfeatures", Kd);
    a = a && a.q;
    ka(a) ? Z.D[G]($, a) : J(50)
}
};
    $.k = function () {
        for (var a = $.K(), b = 0; b < a[y]; b++)a[b].get(V)
    };
    (function () {
        var a = $.N;
        if (!rc(a)) {
            J(16);
            var b = !1, c = function () {
                !b && rc(a) && (b = !0, va(M, "visibilitychange", c))
            };
            L(M, "visibilitychange", c)
        }
    })();
    function La(a) {
        var b = 1, c = 0, d;
        if (a)for (b = 0, d = a[y] - 1; 0 <= d; d--)c = a.charCodeAt(d), b = (b << 6 & 268435455) + c + (c << 14), c = b & 266338304, b = 0 != c ? b ^ c >> 21 : b;
        return b
    }
})(window);
