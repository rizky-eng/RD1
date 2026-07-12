// Bubble generator
function createBubble() {
    const bubblesContainer = document.querySelector('.bubbles');
    if (!bubblesContainer) return;
    
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    
    const size = Math.random() * 40 + 10;
    bubble.style.width = `${size}px`;
    bubble.style.height = `${size}px`;
    bubble.style.left = `${Math.random() * 100}%`;
    bubble.style.animationDuration = `${Math.random() * 5 + 5}s`;
    
    bubblesContainer.appendChild(bubble);
    
    setTimeout(() => {
        bubble.remove();
    }, 10000);
}

// Generate bubbles periodically
setInterval(createBubble, 2000);

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(0, 0, 0, 0.8)';
    } else {
        navbar.style.background = 'rgba(0, 0, 0, 0.3)';
    }
});

// Animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all product cards
document.querySelectorAll('.product-card, .feature').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

console.log('🌊 Sasya Rebreather - Deep Dive Experience Loaded');

// Attempt to open device email client via mailto. If it fails, show fallback modal with webmail options.
function openEmail(to) {
    const subject = encodeURIComponent('Inquiry from Website');
    const body = encodeURIComponent('\n\n--\nThis message was started from the RD1 website contact button.');
    const mailto = `mailto:${to}?subject=${subject}&body=${body}`;

    // Try to navigate to mailto
    window.location.href = mailto;

    // After a short delay, show fallback options for webmail
    setTimeout(() => {
        const modal = document.getElementById('email-fallback-modal');
        if (modal) {
            modal.classList.add('open');
        }
    }, 800);
}

// Open email using an element's href (mailto). Safer when subject is built in the link.
function openEmailFromElement(el) {
    try {
        const href = el.getAttribute('href');
        if (!href) return;
        window.location.href = href;
        setTimeout(() => {
            const modal = document.getElementById('email-fallback-modal');
            if (modal) modal.classList.add('open');
        }, 800);
    } catch (e) {
        console.error('openEmailFromElement error', e);
    }
}

// Close fallback modal
function closeEmailFallback() {
    const modal = document.getElementById('email-fallback-modal');
    if (modal) modal.classList.remove('open');
}

// Close modal when clicking outside content
document.addEventListener('click', (e) => {
    const modal = document.getElementById('email-fallback-modal');
    if (!modal) return;
    if (modal.classList.contains('open')) {
        const content = modal.querySelector('.modal-content');
        if (content && !content.contains(e.target)) {
            closeEmailFallback();
        }
    }
});