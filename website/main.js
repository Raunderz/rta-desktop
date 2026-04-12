import van from "vanjs-core"

const { div, h1, p, img, main, section, a, button } = van.tags

const App = () => {
    // Parallax logic
    let ticking = false;
    window.addEventListener('mousemove', (e) => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const x = (e.clientX / window.innerWidth - 0.5) * 2;
                const y = (e.clientY / window.innerHeight - 0.5) * 2;
                document.body.style.setProperty('--mx', `${x.toFixed(2)}`);
                document.body.style.setProperty('--my', `${y.toFixed(2)}`);
                ticking = false;
            });
            ticking = true;
        }
    });

    return main({ class: "container" },
        section({ class: "hero" },
            div({ class: "title-container" },
                h1({ class: "app-name" }, "rta"),
                p({ class: "description" },
                    "a mobile-first, ai-assisted code editor for android. built for speed, precision, and surgical development on the go."
                )
            ),
            div({ class: "logo-container" },
                img({ class: "logo", src: "/assets/icon.png", alt: "Rta Icon" })
            )
        ),
        div({ class: "cta-container" },
            a({ 
                class: "waitlist-btn", 
                href: "/waitlist.html"
            }, "join waitlist")
        ),
        p({ class: "footer-line" }, "Coming Soon — October 2026")
    )
}

const root = document.getElementById("app")
if (root) {
    van.add(root, App())
}
