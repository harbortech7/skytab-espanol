/* Shared nav + footer injected into every page */
const BASE = '/skytab-espanol';

const NAV_HTML = `
<header id="main-header">
  <a href="${BASE}/" class="nav-logo">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54 54" height="38">
      <circle cx="27" cy="27" r="26" fill="none" stroke="#126ef5" stroke-width="2.5"/>
      <path d="M27 5a22 22 0 1 0 22 22A22.02 22.02 0 0 0 27 5m9.4 23.8v.2c-4.9 1.2-8.8 9.2-9.3 14.7h-.14c-.55-5.5-4.4-13.5-9.26-14.7v-.24A10.6 10.6 0 0 0 26.9 19.5h.18a10.6 10.6 0 0 0 9.32 9.3" fill="#126ef5"/>
    </svg>
    <span>SkyTab</span>
  </a>

  <ul class="nav-links">
    <li class="nav-dropdown">
      <a href="${BASE}/restaurant-types.html">Tipos de Restaurantes</a>
      <div class="dropdown-menu">
        <a href="${BASE}/restaurant-types/table-service.html">Restaurantes de Servicio Completo</a>
        <a href="${BASE}/restaurant-types/quick-service.html">Servicio Rápido</a>
        <a href="${BASE}/restaurant-types/bars.html">Bares y Discotecas</a>
        <a href="${BASE}/restaurant-types/pizzerias.html">Pizzerías</a>
        <a href="${BASE}/restaurant-types/coffee-shops.html">Cafeterías</a>
        <a href="${BASE}/restaurant-types/enterprise.html">Empresas y Multi-Ubicaciones</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="${BASE}/features.html">Características</a>
      <div class="dropdown-menu">
        <a href="${BASE}/features/online-ordering.html">Pedidos en Línea</a>
        <a href="${BASE}/features/mobile-ordering.html">Pedidos y Pagos Móviles</a>
        <a href="${BASE}/features/qr-ordering.html">Orden y Pago por QR</a>
        <a href="${BASE}/features/reservations.html">Reservaciones y Lista de Espera</a>
        <a href="${BASE}/features/loyalty.html">Marketing y Fidelización</a>
        <a href="${BASE}/features/labor.html">Gestión de Personal</a>
        <a href="${BASE}/features/reporting.html">Reportes y Análisis</a>
        <a href="${BASE}/features/integrations.html">Integraciones de Terceros</a>
        <a href="${BASE}/features/website-builder.html">Constructor de Sitio Web</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="${BASE}/pos-hardware.html">Hardware</a>
      <div class="dropdown-menu">
        <a href="${BASE}/pos-hardware/pos-system.html">Sistema POS SkyTab</a>
        <a href="${BASE}/pos-hardware/handheld.html">SkyTab Air (Portátil)</a>
        <a href="${BASE}/pos-hardware/kiosk.html">Quiosco de Autoservicio</a>
        <a href="${BASE}/pos-hardware/kitchen-display.html">Pantalla de Cocina (KDS)</a>
        <a href="${BASE}/pos-hardware/customer-display.html">Pantalla para Clientes</a>
        <a href="${BASE}/pos-hardware/accessories.html">Accesorios POS</a>
      </div>
    </li>
    <li><a href="${BASE}/pricing.html">Precios</a></li>
    <li><a href="${BASE}/reviews.html">Reseñas</a></li>
    <li><a href="${BASE}/blog.html">Blog</a></li>
  </ul>

  <div class="nav-actions">
    <a href="${BASE}/contact.html" class="btn btn-primary">Obtener Demo</a>
    <a href="${BASE}/contact.html" class="btn btn-outline">Construir Sistema</a>
  </div>

  <button class="nav-toggle" id="nav-toggle" aria-label="Menú">
    <span></span><span></span><span></span>
  </button>
</header>

<div class="mobile-menu" id="mobile-menu">
  <a href="${BASE}/">Inicio</a>
  <a href="${BASE}/restaurant-types.html">Tipos de Restaurantes</a>
  <div class="mobile-sub">
    <a href="${BASE}/restaurant-types/table-service.html">Servicio Completo</a>
    <a href="${BASE}/restaurant-types/quick-service.html">Servicio Rápido</a>
    <a href="${BASE}/restaurant-types/bars.html">Bares y Discotecas</a>
    <a href="${BASE}/restaurant-types/pizzerias.html">Pizzerías</a>
    <a href="${BASE}/restaurant-types/coffee-shops.html">Cafeterías</a>
    <a href="${BASE}/restaurant-types/enterprise.html">Empresas Multi-Ubicación</a>
  </div>
  <a href="${BASE}/features.html">Características</a>
  <div class="mobile-sub">
    <a href="${BASE}/features/online-ordering.html">Pedidos en Línea</a>
    <a href="${BASE}/features/mobile-ordering.html">Pedidos Móviles</a>
    <a href="${BASE}/features/qr-ordering.html">Orden por QR</a>
    <a href="${BASE}/features/reservations.html">Reservaciones</a>
    <a href="${BASE}/features/loyalty.html">Marketing y Fidelización</a>
    <a href="${BASE}/features/labor.html">Gestión de Personal</a>
    <a href="${BASE}/features/reporting.html">Reportes</a>
    <a href="${BASE}/features/integrations.html">Integraciones</a>
    <a href="${BASE}/features/website-builder.html">Constructor de Web</a>
  </div>
  <a href="${BASE}/pos-hardware.html">Hardware POS</a>
  <div class="mobile-sub">
    <a href="${BASE}/pos-hardware/pos-system.html">Sistema POS</a>
    <a href="${BASE}/pos-hardware/handheld.html">SkyTab Air</a>
    <a href="${BASE}/pos-hardware/kiosk.html">Quiosco</a>
    <a href="${BASE}/pos-hardware/kitchen-display.html">Pantalla de Cocina</a>
    <a href="${BASE}/pos-hardware/customer-display.html">Pantalla Cliente</a>
    <a href="${BASE}/pos-hardware/accessories.html">Accesorios</a>
  </div>
  <a href="${BASE}/pricing.html">Precios</a>
  <a href="${BASE}/reviews.html">Reseñas</a>
  <a href="${BASE}/blog.html">Blog</a>
  <a href="${BASE}/contact.html" style="margin-top:1rem; display:inline-block; background:var(--blue); color:#fff; padding:.75rem 1.5rem; border-radius:9999px; font-weight:700; text-align:center;">Obtener Demo</a>
</div>
`;

const FOOTER_HTML = `
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="${BASE}/" class="nav-logo" style="margin-bottom:.75rem; display:inline-flex;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54 54" height="36">
            <circle cx="27" cy="27" r="26" fill="none" stroke="#126ef5" stroke-width="2.5"/>
            <path d="M27 5a22 22 0 1 0 22 22A22.02 22.02 0 0 0 27 5m9.4 23.8v.2c-4.9 1.2-8.8 9.2-9.3 14.7h-.14c-.55-5.5-4.4-13.5-9.26-14.7v-.24A10.6 10.6 0 0 0 26.9 19.5h.18a10.6 10.6 0 0 0 9.32 9.3" fill="#126ef5"/>
          </svg>
          <span style="color:#fff; font-weight:800; font-size:1.2rem; margin-left:.4rem;">SkyTab</span>
        </a>
        <p>Sistema POS de nueva generación diseñado para restaurantes. Potenciado por Shift4.</p>
      </div>
      <div class="footer-col">
        <h4>Características</h4>
        <ul>
          <li><a href="${BASE}/features/online-ordering.html">Pedidos en Línea</a></li>
          <li><a href="${BASE}/features/mobile-ordering.html">Pagos Móviles</a></li>
          <li><a href="${BASE}/features/qr-ordering.html">Orden por QR</a></li>
          <li><a href="${BASE}/features/reservations.html">Reservaciones</a></li>
          <li><a href="${BASE}/features/loyalty.html">Marketing y Lealtad</a></li>
          <li><a href="${BASE}/features/labor.html">Gestión de Personal</a></li>
          <li><a href="${BASE}/features/reporting.html">Reportes</a></li>
          <li><a href="${BASE}/features/integrations.html">Integraciones</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Hardware</h4>
        <ul>
          <li><a href="${BASE}/pos-hardware/pos-system.html">Sistema POS</a></li>
          <li><a href="${BASE}/pos-hardware/handheld.html">SkyTab Air</a></li>
          <li><a href="${BASE}/pos-hardware/kiosk.html">Quiosco</a></li>
          <li><a href="${BASE}/pos-hardware/kitchen-display.html">Pantalla de Cocina</a></li>
          <li><a href="${BASE}/pos-hardware/customer-display.html">Pantalla Cliente</a></li>
          <li><a href="${BASE}/pos-hardware/accessories.html">Accesorios</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Empresa</h4>
        <ul>
          <li><a href="${BASE}/pricing.html">Precios</a></li>
          <li><a href="${BASE}/reviews.html">Reseñas</a></li>
          <li><a href="${BASE}/blog.html">Blog</a></li>
          <li><a href="${BASE}/contact.html">Contacto</a></li>
          <li><a href="${BASE}/privacy-policy.html">Política de Privacidad</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2025 SkyTab, una empresa de Shift4. Todos los derechos reservados.</span>
      <a href="${BASE}/privacy-policy.html">Política de Privacidad</a>
    </div>
  </div>
</footer>
`;

// Inject nav + footer
document.addEventListener('DOMContentLoaded', () => {
  // Header
  const headerEl = document.createElement('div');
  headerEl.innerHTML = NAV_HTML;
  document.body.prepend(...headerEl.childNodes);

  // Footer
  const footerEl = document.createElement('div');
  footerEl.innerHTML = FOOTER_HTML;
  document.body.append(...footerEl.childNodes);

  // Scroll header effect
  const header = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  });

  // Mobile menu toggle
  const toggle = document.getElementById('nav-toggle');
  const menu = document.getElementById('mobile-menu');
  toggle?.addEventListener('click', () => {
    menu.classList.toggle('open');
  });

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      item.classList.toggle('open');
    });
  });

  // Scroll reveal
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
});
