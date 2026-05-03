// @ts-check
(function () {
    if (!document.currentScript) {
        return
    }
    const environment = document.currentScript.getAttribute("environment");
    let fetchURL = "https://assets.geeksforgeeks.org/service/latex/";
    if (environment==="local") {
        fetchURL = "./"        
    }
    else if (environment==="development") {
        fetchURL = "https://assets.geeksforgeeks.org/service/latex-dev/"
    }

    /**
     * @typedef {Object} ScriptData
     * @property {string} url
     * @property {string} type
     * @property {boolean} [defer=false]
     * @property {string} [integrity=""]
     * @property {string} [crossOrigin=""]
     */

    /**
     * @type {ScriptData[]}
     */
    var scriptData = [
        {
            url: "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
            type: "stylesheet",
            integrity:
                "sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV",
            crossOrigin: "anonymous",
        },
        {
            url: "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
            type: "text/javascript",
            integrity:
                "sha384-XjKyOOlGwcjNTAIQHIpgOno0Hl1YQqzUOEleOLALmuqehneUG+vnGctmUb0ZY0l8",
            crossOrigin: "anonymous",
            defer: true,
        },
        {
            url: "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js",
            type: "text/javascript",
            integrity:
                "sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05",
            crossOrigin: "anonymous",
            defer: true,
        },
        {
            url: `${fetchURL}index.js`,
            type: "text/javascript",
            defer: true,
        },
    ];

    /**
     * Helper function to load js/css scripts
     *
     * @param {ScriptData} data Object with detail about the script to load
     */
    function loadScript(data) {
        /**
         * @type {HTMLScriptElement | HTMLLinkElement}
         */
        var fileRef = document.createElement("script");
        try {
            if (data.type === "text/javascript") {
                if (data.url) {
                    fileRef.src = data.url;
                }
                if (data.type) {
                    fileRef.type = data.type;
                }
                if (data.integrity) {
                    fileRef.integrity = data.integrity;
                }
                if (data.crossOrigin) {
                    fileRef.crossOrigin = data.crossOrigin;
                }
                if (data.defer) {
                    fileRef.defer = data.defer;
                }
                fileRef.async = false;
            } else {
                fileRef = document.createElement("link");
                if (data.url) {
                    fileRef.href = data.url;
                }
                if (data.type) {
                    fileRef.rel = data.type;
                }
                if (data.integrity) {
                    fileRef.integrity = data.integrity;
                }
                if (data.crossOrigin) {
                    fileRef.crossOrigin = data.crossOrigin;
                }
            }
            if (fileRef) {
                document.body.appendChild(fileRef);
            }
        } catch (error) {
            console.log(error);
        }
    }

    for (var i=0;i<scriptData.length;i++) {
        loadScript(scriptData[i])
    }
})();
