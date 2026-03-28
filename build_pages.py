#!/usr/bin/env python3
"""Generate all site pages for skytab-espanol"""
import os

BASE = '/home/mark/Desktop/skytabmx/site'
ASSET = '/skytab-espanol'

def page(title, meta_desc, body, path):
    os.makedirs(os.path.dirname(f'{BASE}/{path}'), exist_ok=True)
    depth = path.count('/') 
    css_base = ASSET
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | SkyTab España</title>
  <meta name="description" content="{meta_desc}"/>
  <link rel="stylesheet" href="{css_base}/style.css"/>
</head>
<body>
<script src="{css_base}/components.js"></script>
<main style="padding-top:72px">
{body}
</main>
</body>
</html>"""
    with open(f'{BASE}/{path}', 'w') as f:
        f.write(html)
    print(f'  ✓ {path}')

def page_hero(title, subtitle, eyebrow=''):
    ey = f'<div class="eyebrow" style="color:rgba(255,255,255,.7);text-transform:uppercase;letter-spacing:.1em;font-size:.8rem;font-weight:700;margin-bottom:.5rem">{eyebrow}</div>' if eyebrow else ''
    return f"""
<section class="page-hero">
  <div class="container">
    {ey}
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
</section>"""

def cta(heading="¿Listo para Empezar?", sub="Únete a más de 40,000 restaurantes que confían en SkyTab.", btn="Obtener una Demo"):
    return f"""
<section class="bg-blue cta-band">
  <div class="container">
    <div class="reveal">
      <h2 class="text-white">{heading}</h2>
      <p class="text-white">{sub}</p>
      <div class="cta-actions">
        <a href="{ASSET}/contact.html" class="btn" style="background:#fff;color:var(--blue)">{btn}</a>
        <a href="{ASSET}/pricing.html" class="btn btn-outline">Ver Precios</a>
      </div>
    </div>
  </div>
</section>"""

def split(h2, body_html, img_url, img_alt, reverse=False, dark=False):
    bg = 'bg-dark' if dark else 'bg-white'
    cls = 'feature-split reverse' if reverse else 'feature-split'
    return f"""
<section class="{bg} section-pad">
  <div class="container">
    <div class="{cls} reveal">
      <div class="feature-text">
        {h2}
        {body_html}
      </div>
      <div>
        <img src="{img_url}" alt="{img_alt}" style="border-radius:12px;width:100%"/>
      </div>
    </div>
  </div>
</section>"""

# ─── FEATURES.HTML ────────────────────────────────────────────────────────────
features_body = page_hero(
    "Características del POS para Impulsar Tu Negocio",
    "SkyTab es más que un sistema POS. Es una plataforma todo-en-uno con todo lo que necesitas para que tu restaurante prospere.",
    "Plataforma Todo en Uno"
) + """
<section class="bg-offwhite section-pad">
  <div class="container">
    <div class="section-heading reveal">
      <h2>Un Sistema Operativo para Tu Restaurante</h2>
    </div>
    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(300px,1fr)); gap:2rem">

      <a href="/skytab-espanol/features/online-ordering.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp" alt="Pedidos en línea"/>
        <div class="card-body">
          <h3>Pedidos en Línea</h3>
          <div class="orange-bar"></div>
          <p>Tu sitio de pedidos personalizado, comisiones cero, directo a tu POS. Integrado con DoorDash, Uber Eats y más.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/mobile-ordering.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png" alt="Pedidos móviles"/>
        <div class="card-body">
          <h3>Pedidos y Pagos Móviles</h3>
          <div class="orange-bar"></div>
          <p>Permite a tus clientes pedir y pagar desde su teléfono, directamente en la mesa.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/qr-ordering.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp" alt="Código QR"/>
        <div class="card-body">
          <h3>Orden y Pago por Código QR</h3>
          <div class="orange-bar"></div>
          <p>Tecnología sin contacto que acelera el servicio y mejora la experiencia del cliente.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/reservations.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/01e87f0da06975dc8b67700bd190f3b6d640ce89-1100x700.png" alt="Reservaciones"/>
        <div class="card-body">
          <h3>Reservaciones y Lista de Espera</h3>
          <div class="orange-bar"></div>
          <p>Gestión centralizada de mesas, reservaciones en línea y lista de espera digital.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/loyalty.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/ff2922160f7797d6b0f6525bff2cbfc75e0b6e6e-1100x700.png" alt="Marketing y Lealtad"/>
        <div class="card-body">
          <h3>Marketing y Fidelización</h3>
          <div class="orange-bar"></div>
          <p>Programas de puntos, tarjetas de regalo, campañas de email y mucho más para retener clientes.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/labor.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/52e29e564ee16f05790a418bffff59a37159fadd-1100x700.png" alt="Gestión de Personal"/>
        <div class="card-body">
          <h3>Gestión de Personal y Nóminas</h3>
          <div class="orange-bar"></div>
          <p>Programación de turnos, control de tiempo y gestión de propinas desde un solo lugar.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/reporting.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp" alt="Reportes"/>
        <div class="card-body">
          <h3>Reportes y Análisis</h3>
          <div class="orange-bar"></div>
          <p>Datos en tiempo real para tomar decisiones inteligentes y mejorar tu rentabilidad.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/integrations.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp" alt="Integraciones"/>
        <div class="card-body">
          <h3>Integraciones de Terceros</h3>
          <div class="orange-bar"></div>
          <p>Conecta con más de 200 apps populares: contabilidad, delivery, reservaciones y más.</p>
        </div>
      </a>

      <a href="/skytab-espanol/features/website-builder.html" class="card" style="text-decoration:none; color:inherit; display:block; transition:transform .2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png" alt="Constructor Web"/>
        <div class="card-body">
          <h3>Constructor de Sitio Web con IA</h3>
          <div class="orange-bar"></div>
          <p>Crea el sitio web de tu restaurante con inteligencia artificial. Sin código, sin complicaciones.</p>
        </div>
      </a>

    </div>
  </div>
</section>
""" + cta()
page("Características del POS para Restaurantes", "Descubre todas las características de SkyTab: pedidos en línea, mobile, QR, reservaciones, marketing y mucho más.", features_body, "features.html")

# ─── PRICING.HTML ──────────────────────────────────────────────────────────────
pricing_body = page_hero(
    "Precios Simples y Transparentes",
    "Sin contratos. Sin tarifas ocultas. Comienza por $0 y escala según tus necesidades.",
    "Precios POS"
) + """
<section class="bg-offwhite section-pad">
  <div class="container">
    <div class="section-heading reveal">
      <h2>Elige el Plan Correcto para Tu Negocio</h2>
      <p>Todos los planes incluyen hardware, software y pagos. Sin tarifas de instalación.</p>
    </div>
    <div class="pricing-grid reveal">
      <div class="pricing-card">
        <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em">Estándar</div>
        <div class="price"><sup>$</sup>29.99</div>
        <div class="per">por mes por terminal</div>
        <ul>
          <li>Software POS completo</li>
          <li>Pedidos en línea GRATIS</li>
          <li>Marketing y fidelización GRATIS</li>
          <li>Reservaciones y lista de espera</li>
          <li>Reportes y análisis</li>
          <li>Soporte 24/7</li>
          <li>Garantía de por vida en hardware</li>
        </ul>
        <a href="/skytab-espanol/contact.html" class="btn btn-outline-blue" style="width:100%;display:block;text-align:center">Comenzar</a>
      </div>

      <div class="pricing-card featured">
        <div class="eyebrow" style="color:rgba(255,255,255,.7);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em">Más Popular</div>
        <div class="eyebrow" style="font-size:1rem;font-weight:800;margin-bottom:.5rem">Ventaja</div>
        <div class="price"><sup>$</sup>0</div>
        <div class="per">con el Programa Advantage</div>
        <ul>
          <li>Todo lo del plan Estándar</li>
          <li>Hardware POS incluido</li>
          <li>Instalación incluida</li>
          <li>Programa de precios de conveniencia</li>
          <li>Sin cargos mensuales de software</li>
          <li>Soporte prioritario 24/7</li>
          <li>Gestor de cuenta dedicado</li>
        </ul>
        <a href="/skytab-espanol/contact.html" class="btn" style="background:#fff;color:var(--blue);width:100%;display:block;text-align:center">Comenzar por $0</a>
      </div>

      <div class="pricing-card">
        <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em">Empresarial</div>
        <div class="price">Custom</div>
        <div class="per">cotización personalizada</div>
        <ul>
          <li>Todo lo del plan Ventaja</li>
          <li>Multi-ubicaciones ilimitadas</li>
          <li>Dashboard centralizado</li>
          <li>Integración API personalizada</li>
          <li>Gestor de cuenta dedicado</li>
          <li>Onboarding personalizado</li>
          <li>SLA garantizado</li>
        </ul>
        <a href="/skytab-espanol/contact.html" class="btn btn-outline-blue" style="width:100%;display:block;text-align:center">Solicitar Cotización</a>
      </div>
    </div>
  </div>
</section>

<section class="bg-white section-pad">
  <div class="container" style="max-width:800px">
    <div class="section-heading reveal">
      <h2>Preguntas Frecuentes sobre Precios</h2>
    </div>
    <div class="reveal">
      <div class="faq-item">
        <button class="faq-q">¿Hay contratos a largo plazo?</button>
        <div class="faq-a">No. SkyTab opera mes a mes sin contratos de largo plazo. Puedes cancelar en cualquier momento sin penalizaciones.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Qué incluye el Programa Advantage ($0)?</button>
        <div class="faq-a">El Programa Advantage incluye hardware POS, instalación, software y soporte — todo por $0 por mes. Funciona a través de un pequeño cargo de conveniencia aplicado a las transacciones con tarjeta de crédito, que los restaurantes pueden trasladar a los clientes.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Incluye el procesamiento de pagos?</button>
        <div class="faq-a">Sí. El procesamiento de pagos está integrado con tarifas competitivas. Las tarifas exactas dependen del volumen de tu negocio.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Qué pasa si necesito más terminales?</button>
        <div class="faq-a">Puedes agregar terminales adicionales por $29.99/mes cada una. Para multi-ubicaciones, consulta nuestro plan Empresarial para descuentos de volumen.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Ofrecen periodo de prueba?</button>
        <div class="faq-a">Sí, podemos agendar una demo completa del sistema. Contáctanos para conocer las opciones de prueba disponibles para tu tipo de negocio.</div>
      </div>
    </div>
  </div>
</section>
""" + cta("¿Preguntas sobre Precios?", "Nuestros especialistas están listos para ayudarte a elegir el plan perfecto.", "Hablar con un Especialista")
page("Precios del Sistema POS", "Precios simples y transparentes para el sistema POS de SkyTab. Desde $0 con el Programa Advantage.", pricing_body, "pricing.html")

# ─── RESTAURANT-TYPES.HTML ────────────────────────────────────────────────────
rt_body = page_hero(
    "El POS Correcto para Tu Tipo de Restaurante",
    "SkyTab se adapta a cada tipo de establecimiento. Desde restaurantes de servicio completo hasta cafeterías y grandes empresas.",
    "Tipos de Restaurantes"
) + """
<section class="bg-offwhite section-pad">
  <div class="container">
    <div class="cards-grid-2 reveal">

      <a href="/skytab-espanol/restaurant-types/table-service.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/3d6c76806dbf4f621f8a108717641ab7210a505c-2196x935.png" alt="Restaurantes de Servicio Completo"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Servicio Completo</div>
          <h3>Restaurantes de Servicio Completo</h3>
          <div class="orange-bar"></div>
          <p>Software POS diseñado para optimizar el servicio en mesa, gestión de menú y la experiencia del comensal en restaurantes formales e informales.</p>
        </div>
      </a>

      <a href="/skytab-espanol/restaurant-types/quick-service.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp" alt="Servicio Rápido"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Quick Service</div>
          <h3>Restaurantes de Servicio Rápido</h3>
          <div class="orange-bar"></div>
          <p>Quioscos de autoservicio, pantallas de cocina y pedidos en línea diseñados para acelerar el servicio y reducir tiempos de espera.</p>
        </div>
      </a>

      <a href="/skytab-espanol/restaurant-types/bars.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png" alt="Bares y Discotecas"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Bares</div>
          <h3>Bares y Discotecas</h3>
          <div class="orange-bar"></div>
          <p>Pestañas de bar rápidas, división de cuentas y gestión de inventario de bebidas para mantener el ritmo en los momentos más concurridos.</p>
        </div>
      </a>

      <a href="/skytab-espanol/restaurant-types/pizzerias.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp" alt="Pizzerías"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Pizzerías</div>
          <h3>Pizzerías y Pasta</h3>
          <div class="orange-bar"></div>
          <p>Gestión de pedidos para llevar, entrega a domicilio y para comer en el local con seguimiento de tiempo de horneado integrado.</p>
        </div>
      </a>

      <a href="/skytab-espanol/restaurant-types/coffee-shops.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/01e87f0da06975dc8b67700bd190f3b6d640ce89-1100x700.png" alt="Cafeterías"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Cafeterías</div>
          <h3>Cafeterías y Tiendas de Té</h3>
          <div class="orange-bar"></div>
          <p>Líneas de servicio rápido, pedidos personalizados y programas de fidelidad para aumentar las visitas de tus clientes habituales.</p>
        </div>
      </a>

      <a href="/skytab-espanol/restaurant-types/enterprise.html" class="card" style="text-decoration:none;color:inherit;transition:transform .2s" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
        <img class="card-img" src="https://cdn.sanity.io/images/2nz3tcxf/production/ff2922160f7797d6b0f6525bff2cbfc75e0b6e6e-1100x700.png" alt="Empresas"/>
        <div class="card-body">
          <div class="eyebrow" style="color:var(--blue);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem">Empresarial</div>
          <h3>Cadenas y Multi-Ubicaciones</h3>
          <div class="orange-bar"></div>
          <p>Panel centralizado para gestionar múltiples sucursales, reportes consolidados y configuración de menú sincronizada en toda la empresa.</p>
        </div>
      </a>

    </div>
  </div>
</section>
""" + cta()
page("POS para Todo Tipo de Restaurante", "SkyTab tiene el sistema POS ideal para tu tipo de restaurante: servicio completo, rápido, bares, pizzerías, cafeterías y empresas.", rt_body, "restaurant-types.html")

# ─── POS-HARDWARE.HTML ────────────────────────────────────────────────────────
hw_body = page_hero(
    "Hardware POS Diseñado para Restaurantes",
    "Hardware comercial resistente con garantía de por vida. Diseñado para los entornos más exigentes.",
    "Hardware POS"
) + """
<section class="bg-white section-pad">
  <div class="container">
    <div class="cards-grid-3 reveal">
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/11f456621c4c1f710ca70d2e47017fdcfa6bc1ef-660x728.png" alt="Sistema POS SkyTab"/>
        <h3>Sistema POS SkyTab</h3>
        <div class="hw-divider"></div>
        <p>Estación de trabajo elegante con pantalla de alta resolución, procesador potente y garantía de por vida. El corazón de tu operación.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/pos-system.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/c54506cb23720c00b8b18f401316f1478652d51c-660x728.png" alt="SkyTab Air"/>
        <h3>SkyTab Air</h3>
        <div class="hw-divider"></div>
        <p>Terminal portátil que acepta pagos en la mesa, en la acera o en entrega a domicilio. Batería de larga duración para turnos completos.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/handheld.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/86517e9451348964de67b3210117b6b728c3cf63-660x728.png" alt="SkyTab Glass"/>
        <h3>SkyTab Glass</h3>
        <div class="hw-divider"></div>
        <p>Tablet Android optimizada para tomar pedidos. Perfecta para el personal de piso que necesita movilidad y rapidez.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/handheld.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/611f0e498abdaf16b56b10d01d89b31055c38aa8-1007x798.png" alt="Quiosco de Autoservicio"/>
        <h3>Quiosco de Autoservicio</h3>
        <div class="hw-divider"></div>
        <p>Permite a los clientes ordenar y pagar solos. Reduce tiempos de espera y aumenta el ticket promedio con sugerencias automáticas.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/kiosk.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/52e29e564ee16f05790a418bffff59a37159fadd-1100x700.png" alt="Pantalla de Cocina KDS"/>
        <h3>Pantalla de Cocina (KDS)</h3>
        <div class="hw-divider"></div>
        <p>Pantalla de cocina digital resistente que elimina el papel. Muestra los pedidos en tiempo real y mejora la comunicación entre cocina y sala.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/kitchen-display.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
      <div class="hw-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp" alt="Pantalla para Clientes"/>
        <h3>Pantalla para Clientes</h3>
        <div class="hw-divider"></div>
        <p>Pantalla orientada al cliente que muestra el resumen del pedido y acepta propinas digitales. Aumenta la satisfacción y transparencia.</p>
        <div style="margin-top:1.5rem"><a href="/skytab-espanol/pos-hardware/customer-display.html" class="btn btn-outline-blue">Ver Más</a></div>
      </div>
    </div>
  </div>
</section>

<section class="bg-dark section-pad">
  <div class="container">
    <div class="section-heading reveal">
      <h2 class="text-white">¿Por Qué Elegir el Hardware de SkyTab?</h2>
    </div>
    <div class="cards-grid-4 reveal">
      <div style="text-align:center;color:#fff;padding:1.5rem">
        <div style="font-size:2.5rem;margin-bottom:.75rem">🔒</div>
        <h3 style="color:#fff;margin-bottom:.5rem">Garantía de Por Vida</h3>
        <p style="color:rgba(255,255,255,.65);font-size:.9rem">Todo nuestro hardware incluye garantía de por vida sin costo adicional.</p>
      </div>
      <div style="text-align:center;color:#fff;padding:1.5rem">
        <div style="font-size:2.5rem;margin-bottom:.75rem">⚡</div>
        <h3 style="color:#fff;margin-bottom:.5rem">Grado Comercial</h3>
        <p style="color:rgba(255,255,255,.65);font-size:.9rem">Construido para entornos de restaurante exigentes con alta resistencia y durabilidad.</p>
      </div>
      <div style="text-align:center;color:#fff;padding:1.5rem">
        <div style="font-size:2.5rem;margin-bottom:.75rem">🔧</div>
        <h3 style="color:#fff;margin-bottom:.5rem">Instalación Incluida</h3>
        <p style="color:rgba(255,255,255,.65);font-size:.9rem">Técnicos certificados instalan y configuran todo en tu restaurante.</p>
      </div>
      <div style="text-align:center;color:#fff;padding:1.5rem">
        <div style="font-size:2.5rem;margin-bottom:.75rem">🔄</div>
        <h3 style="color:#fff;margin-bottom:.5rem">Actualizaciones Gratis</h3>
        <p style="color:rgba(255,255,255,.65);font-size:.9rem">Software siempre actualizado automáticamente sin costo adicional.</p>
      </div>
    </div>
  </div>
</section>
""" + cta("Listo para Modernizar Tu Restaurante", "Habla con un especialista para encontrar el hardware perfecto para tu operación.")
page("Hardware POS para Restaurantes", "Descubre el hardware POS de SkyTab: terminales, portátiles, quioscos, pantallas de cocina y accesorios con garantía de por vida.", hw_body, "pos-hardware.html")

# ─── CONTACT.HTML ─────────────────────────────────────────────────────────────
contact_body = page_hero(
    "Contacta con Nuestro Equipo",
    "¿Listo para transformar tu restaurante? Cuéntanos sobre tu negocio y te contactaremos en menos de 24 horas.",
    "Contacto"
) + """
<section class="bg-offwhite section-pad">
  <div class="container" style="max-width:900px">
    <div style="display:grid; grid-template-columns:1fr 1.5fr; gap:4rem; align-items:start" class="reveal">
      <div>
        <h2 style="font-size:1.75rem; margin-bottom:1.5rem">Habla con un Especialista</h2>
        <p style="color:var(--muted); margin-bottom:2rem">Nuestros especialistas en POS para restaurantes están listos para mostrarte cómo SkyTab puede transformar tu negocio.</p>
        <div style="display:flex;flex-direction:column;gap:1.5rem">
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="width:48px;height:48px;background:var(--blue);border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:#fff;font-size:1.2rem">📞</div>
            <div>
              <div style="font-weight:700;margin-bottom:.2rem">Llámanos</div>
              <div style="color:var(--muted);font-size:.9rem">Disponible 24/7 para soporte</div>
            </div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="width:48px;height:48px;background:var(--blue);border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:#fff;font-size:1.2rem">✉️</div>
            <div>
              <div style="font-weight:700;margin-bottom:.2rem">Escríbenos</div>
              <div style="color:var(--muted);font-size:.9rem">Respuesta en menos de 24 horas</div>
            </div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="width:48px;height:48px;background:var(--blue);border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:#fff;font-size:1.2rem">💬</div>
            <div>
              <div style="font-weight:700;margin-bottom:.2rem">Chat en Vivo</div>
              <div style="color:var(--muted);font-size:.9rem">Respuesta inmediata durante horario laboral</div>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-body" style="padding:2.5rem">
          <h3 style="margin-bottom:1.5rem">Solicitar una Demo</h3>
          <form action="/contact-submit" method="POST">
            <div class="form-grid">
              <div class="form-group">
                <label for="first_name">Nombre</label>
                <input type="text" id="first_name" name="first_name" placeholder="Juan" required/>
              </div>
              <div class="form-group">
                <label for="last_name">Apellido</label>
                <input type="text" id="last_name" name="last_name" placeholder="García" required/>
              </div>
              <div class="form-group">
                <label for="email">Correo Electrónico</label>
                <input type="email" id="email" name="email" placeholder="juan@restaurante.com" required/>
              </div>
              <div class="form-group">
                <label for="phone">Teléfono</label>
                <input type="tel" id="phone" name="phone" placeholder="+34 600 000 000"/>
              </div>
              <div class="form-group full">
                <label for="business_name">Nombre del Restaurante</label>
                <input type="text" id="business_name" name="business_name" placeholder="Restaurante El Jardín" required/>
              </div>
              <div class="form-group full">
                <label for="restaurant_type">Tipo de Restaurante</label>
                <select id="restaurant_type" name="restaurant_type">
                  <option value="">Selecciona una opción</option>
                  <option value="full_service">Servicio Completo</option>
                  <option value="quick_service">Servicio Rápido / QSR</option>
                  <option value="bar">Bar o Discoteca</option>
                  <option value="pizzeria">Pizzería</option>
                  <option value="cafe">Cafetería</option>
                  <option value="enterprise">Cadena / Multi-Ubicación</option>
                  <option value="other">Otro</option>
                </select>
              </div>
              <div class="form-group full">
                <label for="locations">Número de Ubicaciones</label>
                <select id="locations" name="locations">
                  <option value="1">1 ubicación</option>
                  <option value="2-5">2 – 5 ubicaciones</option>
                  <option value="6-20">6 – 20 ubicaciones</option>
                  <option value="20+">Más de 20 ubicaciones</option>
                </select>
              </div>
              <div class="form-group full">
                <label for="message">¿Cómo podemos ayudarte?</label>
                <textarea id="message" name="message" placeholder="Cuéntanos sobre tu negocio y lo que necesitas..."></textarea>
              </div>
            </div>
            <div class="form-submit">
              <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Enviar Solicitud</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-dark section-pad-sm">
  <div class="container">
    <div class="stats-bar" style="background:none;gap:0">
      <div class="stat-item" style="background:transparent">
        <div class="stat-num">40K+</div>
        <div class="stat-label">Restaurantes activos</div>
      </div>
      <div class="stat-item" style="background:transparent">
        <div class="stat-num">24/7</div>
        <div class="stat-label">Soporte disponible</div>
      </div>
      <div class="stat-item" style="background:transparent">
        <div class="stat-num">&lt; 24h</div>
        <div class="stat-label">Tiempo de respuesta</div>
      </div>
      <div class="stat-item" style="background:transparent">
        <div class="stat-num">4.8★</div>
        <div class="stat-label">Calificación promedio</div>
      </div>
    </div>
  </div>
</section>
"""
page("Contacto – Solicitar Demo", "Contacta con el equipo de SkyTab para solicitar una demo personalizada de nuestro sistema POS para restaurantes.", contact_body, "contact.html")

# ─── REVIEWS.HTML ─────────────────────────────────────────────────────────────
reviews_body = page_hero(
    "Lo Que Dicen Nuestros Clientes",
    "Miles de propietarios de restaurantes confían en SkyTab. Lee sus historias de éxito.",
    "Reseñas y Testimonios"
) + """
<section class="bg-offwhite section-pad">
  <div class="container">
    <div class="trust-row reveal" style="margin-bottom:3rem">
      <div style="text-align:center">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/59b2939978d757e3f6f556642caae721ef4959cb-245x116.png" alt="Capterra 4.7" style="max-height:80px"/>
      </div>
      <div style="text-align:center">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/0c0cf19b256370e03eed77906bb5c6e934192618-245x116.png" alt="Software Advice 4.7" style="max-height:80px"/>
      </div>
      <div style="text-align:center">
        <div style="font-size:2rem;color:#fbbf24">★★★★★</div>
        <div style="font-weight:700">4.8 / 5 en Google</div>
        <div style="font-size:.8rem;color:var(--muted)">+2,400 reseñas</div>
      </div>
    </div>
    <div class="cards-grid-3 reveal">
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"SkyTab ha transformado completamente las operaciones de nuestro restaurante. La facilidad de uso es impresionante y el soporte al cliente es simplemente increíble."</p>
        <div class="reviewer">Carlos M.</div>
        <div class="reviewer-role">Propietario, Restaurante El Jardín – Madrid</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Los pedidos en línea gratuitos solos valieron la pena. Ahorramos más de €400 al mes en comisiones de plataformas de terceros. El retorno de inversión fue inmediato."</p>
        <div class="reviewer">Ana L.</div>
        <div class="reviewer-role">Gerente, Café Madrileño – Barcelona</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Pasamos de 3 sistemas diferentes a SkyTab y nunca miramos atrás. Es completo, confiable y el precio es muy justo para todo lo que ofrece."</p>
        <div class="reviewer">Roberto S.</div>
        <div class="reviewer-role">Director, Grupo La Hacienda – Valencia</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"La implementación fue rápida y el equipo de soporte nos guió en todo momento. En 2 días ya estábamos operando al 100%. Muy recomendado."</p>
        <div class="reviewer">María G.</div>
        <div class="reviewer-role">Propietaria, Pizzería Napoli – Sevilla</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"El módulo de fidelización nos ha permitido aumentar la frecuencia de visitas de nuestros clientes en un 35%. Los reportes son muy detallados y fáciles de entender."</p>
        <div class="reviewer">Diego P.</div>
        <div class="reviewer-role">CEO, Cafeterías Aroma – Cadena de 8 locales</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"El SkyTab Air ha cambiado la forma en que atendemos las mesas. Los clientes aman poder ver y pagar su cuenta desde la comodidad de su asiento."</p>
        <div class="reviewer">Laura F.</div>
        <div class="reviewer-role">Propietaria, Bar La Terraza – Málaga</div>
      </div>
    </div>
  </div>
</section>
""" + cta("¿Te Convencieron las Reseñas?", "Únete a miles de restaurantes satisfechos con SkyTab.", "Solicitar Demo Gratis")
page("Reseñas del Sistema POS SkyTab", "Lee las reseñas y testimonios de propietarios de restaurantes que usan SkyTab como su sistema POS.", reviews_body, "reviews.html")

# ─── BLOG.HTML ────────────────────────────────────────────────────────────────
blog_body = page_hero(
    "Blog y Recursos para Restaurantes",
    "Guías, consejos y tendencias de la industria para ayudarte a hacer crecer tu restaurante.",
    "Blog"
) + """
<section class="bg-white section-pad">
  <div class="container">
    <div class="cards-grid-3 reveal">
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/3d6c76806dbf4f621f8a108717641ab7210a505c-2196x935.png" alt="IA para restaurantes"/>
        <div class="blog-card-body">
          <div class="tag">Tecnología</div>
          <h3>Cómo la Inteligencia Artificial Está Transformando los Restaurantes</h3>
          <p>Descubre cómo los restaurantes están usando IA para optimizar menús, predecir demanda y personalizar la experiencia del cliente.</p>
        </div>
      </a>
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp" alt="Pedidos en línea"/>
        <div class="blog-card-body">
          <div class="tag">Pedidos en Línea</div>
          <h3>Guía Completa: Cómo Configurar los Pedidos en Línea para Tu Restaurante</h3>
          <p>Paso a paso para lanzar tu propio canal de pedidos en línea y dejar de depender de plataformas de terceros con altas comisiones.</p>
        </div>
      </a>
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png" alt="Programa de fidelidad"/>
        <div class="blog-card-body">
          <div class="tag">Marketing</div>
          <h3>Programas de Fidelización para Restaurantes: Todo lo que Necesitas Saber</h3>
          <p>Cómo crear y gestionar un programa de lealtad que realmente funcione y aumente la frecuencia de visitas de tus clientes.</p>
        </div>
      </a>
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/ff2922160f7797d6b0f6525bff2cbfc75e0b6e6e-1100x700.png" alt="Gestión de personal"/>
        <div class="blog-card-body">
          <div class="tag">Operaciones</div>
          <h3>Gestión Efectiva de Personal en Restaurantes: 10 Estrategias Clave</h3>
          <p>Desde la programación de turnos hasta la retención de empleados, estas estrategias te ayudarán a crear un equipo sólido.</p>
        </div>
      </a>
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp" alt="Costos POS"/>
        <div class="blog-card-body">
          <div class="tag">Finanzas</div>
          <h3>¿Cuánto Cuesta un Sistema POS para Restaurantes en 2025?</h3>
          <p>Análisis detallado de los costos de diferentes sistemas POS del mercado y cómo elegir la mejor opción para tu presupuesto.</p>
        </div>
      </a>
      <a href="#" class="blog-card">
        <img src="https://cdn.sanity.io/images/2nz3tcxf/production/01e87f0da06975dc8b67700bd190f3b6d640ce89-1100x700.png" alt="Quioscos autoservicio"/>
        <div class="blog-card-body">
          <div class="tag">Hardware</div>
          <h3>Quioscos de Autoservicio: ¿Vale la Pena Invertir para Tu Restaurante?</h3>
          <p>Analizamos el ROI de los quioscos de autoservicio y en qué tipos de establecimientos generan mayor rentabilidad.</p>
        </div>
      </a>
    </div>
  </div>
</section>
""" + cta()
page("Blog para Restaurantes", "Artículos, guías y recursos para propietarios y gerentes de restaurantes sobre tecnología, operaciones y marketing.", blog_body, "blog.html")

# ─── PRIVACY-POLICY.HTML ──────────────────────────────────────────────────────
privacy_body = page_hero("Política de Privacidad", "Última actualización: enero 2025") + """
<section class="bg-white section-pad">
  <div class="container" style="max-width:760px">
    <div class="reveal" style="line-height:1.85; color:var(--text)">
      <h2 style="margin-bottom:1rem;font-size:1.5rem">1. Información que Recopilamos</h2>
      <p style="margin-bottom:1.5rem">Recopilamos información que usted nos proporciona directamente, información que recopilamos automáticamente cuando usa nuestros servicios, e información de fuentes de terceros.</p>

      <h2 style="margin-bottom:1rem;font-size:1.5rem">2. Uso de la Información</h2>
      <p style="margin-bottom:1.5rem">Usamos la información que recopilamos para proporcionar, mantener y mejorar nuestros servicios, procesar transacciones, enviar comunicaciones de marketing (con su consentimiento) y cumplir con obligaciones legales.</p>

      <h2 style="margin-bottom:1rem;font-size:1.5rem">3. Compartir Información</h2>
      <p style="margin-bottom:1.5rem">No vendemos su información personal. Podemos compartir información con proveedores de servicios de confianza que nos ayudan a operar nuestro negocio, siempre bajo acuerdos de confidencialidad.</p>

      <h2 style="margin-bottom:1rem;font-size:1.5rem">4. Seguridad de Datos</h2>
      <p style="margin-bottom:1.5rem">Implementamos medidas de seguridad técnicas y organizativas apropiadas para proteger su información contra acceso no autorizado, alteración, divulgación o destrucción.</p>

      <h2 style="margin-bottom:1rem;font-size:1.5rem">5. Sus Derechos</h2>
      <p style="margin-bottom:1.5rem">Usted tiene derecho a acceder, corregir o eliminar su información personal. Para ejercer estos derechos, contáctenos a través de nuestro formulario de contacto.</p>

      <h2 style="margin-bottom:1rem;font-size:1.5rem">6. Contacto</h2>
      <p>Si tiene preguntas sobre esta Política de Privacidad, contáctenos en <a href="/skytab-espanol/contact.html" style="color:var(--blue)">nuestra página de contacto</a>.</p>
    </div>
  </div>
</section>
"""
page("Política de Privacidad", "Política de privacidad de SkyTab España.", privacy_body, "privacy-policy.html")

print("\n✅ Main pages done")

# ─── FEATURE SUB-PAGES ────────────────────────────────────────────────────────
feature_pages = [
    ("online-ordering", "Pedidos en Línea", "Tus Pedidos, Tus Reglas",
     "Lanza tu propio canal de pedidos en línea sin comisiones. Integra con las principales plataformas de delivery.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp",
     ["Tu menú en línea personalizado", "Cero comisiones por pedido", "Integración con DoorDash y Uber Eats", "Pedidos a la mesa con QR", "Menú digital actualizable en tiempo real", "Estadísticas de pedidos en tiempo real"]),
    ("mobile-ordering", "Pedidos y Pagos Móviles", "Paga y Pide Desde Cualquier Lugar",
     "Tus clientes pueden ver el menú, pedir y pagar directamente desde su smartphone, sin apps adicionales.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png",
     ["Sin descarga de apps requerida", "Pagos seguros por NFC y QR", "Envío de ticket digital", "Acepta propinas digitales", "Funciona en cualquier smartphone", "Integración directa con el POS"]),
    ("qr-ordering", "Orden y Pago por Código QR", "Tecnología Sin Contacto Moderna",
     "Solución de orden y pago sin contacto que acelera el servicio y mejora la experiencia de tus clientes.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp",
     ["Código QR personalizado por mesa", "Menú digital interactivo", "Pago sin contacto integrado", "Reduce el tiempo de espera", "Aumenta el ticket promedio", "Actualizaciones de menú instantáneas"]),
    ("reservations", "Reservaciones y Lista de Espera", "Gestión de Mesas Simplificada",
     "Sistema centralizado de reservaciones y lista de espera digital para maximizar la ocupación de tu restaurante.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/01e87f0da06975dc8b67700bd190f3b6d640ce89-1100x700.png",
     ["Reservaciones en línea 24/7", "Lista de espera digital con SMS", "Gestión de distribución de mesas", "Recordatorios automáticos", "Integración con Google y Yelp", "Reportes de ocupación"]),
    ("loyalty", "Marketing y Fidelización", "Clientes que Regresan una y Otra Vez",
     "Programa de lealtad, tarjetas de regalo y campañas de email marketing para aumentar la frecuencia de visitas.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/ff2922160f7797d6b0f6525bff2cbfc75e0b6e6e-1100x700.png",
     ["Programa de puntos personalizado", "Tarjetas de regalo digitales y físicas", "Campañas de email y SMS", "Segmentación de clientes", "Cupones y promociones automáticas", "Análisis de comportamiento del cliente"]),
    ("labor", "Gestión de Personal", "Tu Equipo, Perfectamente Organizado",
     "Programación de turnos, control de tiempo, gestión de propinas y nóminas integradas en un solo lugar.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/52e29e564ee16f05790a418bffff59a37159fadd-1100x700.png",
     ["Programación de turnos inteligente", "Control de asistencia integrado", "Gestión de propinas automatizada", "Integración con sistemas de nómina", "App para empleados", "Alertas de horas extras"]),
    ("reporting", "Reportes y Análisis", "Decisiones Basadas en Datos Reales",
     "Dashboard completo con reportes de ventas, inventario, personal y rendimiento en tiempo real.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp",
     ["Dashboard en tiempo real", "Reportes de ventas por período", "Análisis de artículos del menú", "Control de inventario", "Reportes de personal y turnos", "Acceso remoto desde cualquier dispositivo"]),
    ("integrations", "Integraciones de Terceros", "Conecta Todo Tu Ecosistema",
     "SkyTab se integra con más de 200 aplicaciones populares de contabilidad, delivery, reservaciones y más.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp",
     ["QuickBooks y Xero", "DoorDash, Uber Eats, Grubhub", "OpenTable y Resy", "7shifts y HotSchedules", "Compeat y Restaurant365", "API abierta para integraciones custom"]),
    ("website-builder", "Constructor de Sitio Web con IA", "Tu Restaurante en Línea en Minutos",
     "Crea el sitio web profesional de tu restaurante con inteligencia artificial. Sin conocimientos técnicos necesarios.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png",
     ["Diseño generado por IA", "Menú digital integrado", "Pedidos en línea directo", "Optimizado para móviles y SEO", "Dominio personalizado incluido", "Actualizaciones automáticas"]),
]

for slug, title, h2, sub, img, feats in feature_pages:
    feat_li = ''.join(f'<li>{f}</li>' for f in feats)
    body = page_hero(title, sub, "Características") + f"""
<section class="bg-white section-pad">
  <div class="container">
    <div class="feature-split reveal">
      <div class="feature-text">
        <h2>{h2}</h2>
        <div class="orange-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;margin-bottom:1.5rem">{sub}</p>
        <ul class="feature-list">{feat_li}</ul>
        <a href="/skytab-espanol/contact.html" class="btn btn-primary">Obtener una Demo</a>
      </div>
      <div><img src="{img}" alt="{title}" style="border-radius:12px;width:100%"/></div>
    </div>
  </div>
</section>
""" + cta()
    page(title, sub, body, f"features/{slug}.html")

print("✅ Feature pages done")

# ─── RESTAURANT TYPE SUB-PAGES ────────────────────────────────────────────────
rt_pages = [
    ("table-service", "Restaurantes de Servicio Completo",
     "El POS que Eleva Cada Experiencia Gastronómica",
     "Software POS diseñado para restaurantes de servicio completo que buscan optimizar el servicio, la gestión de mesas y la rentabilidad.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/3d6c76806dbf4f621f8a108717641ab7210a505c-2196x935.png",
     ["Gestión de mesas en tiempo real", "División de cuentas flexible", "Pedidos desde la mesa con SkyTab Air", "Menú con modificadores ilimitados", "Historial de clientes y preferencias", "Integración con sistema de reservaciones"]),
    ("quick-service", "Restaurantes de Servicio Rápido",
     "Velocidad y Eficiencia en Cada Pedido",
     "Soluciones POS diseñadas para maximizar la velocidad del servicio y reducir los tiempos de espera.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp",
     ["Quioscos de autoservicio", "Pantallas de cocina KDS", "Pedidos en línea con pickup integrado", "Gestión de fila de espera digital", "Integración con delivery apps", "Menú digital con imágenes"]),
    ("bars", "Bares y Discotecas",
     "El POS que Nunca Para, Como Tu Bar",
     "Sistema POS diseñado para el ritmo acelerado de bares y discotecas, con funciones específicas para el servicio de bebidas.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/1d4c15b4c0031134bb6438830aa475682e2affcc-1100x700.png",
     ["Pestañas de bar rápidas", "Control de bebidas y licores", "División de cuentas entre grupos", "Verificación de edad integrada", "Gestión de eventos especiales", "Reportes de inventario de bebidas"]),
    ("pizzerias", "Pizzerías",
     "El POS Perfecto para Tu Pizzería",
     "Gestión de pedidos para llevar, delivery y para comer en el local, todo desde un solo sistema.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp",
     ["Seguimiento de tiempo de horneado", "Personalización de pizzas ilimitada", "Pedidos para delivery integrados", "Mapa de zona de entrega", "Gestión de conductores de delivery", "Historial de pedidos del cliente"]),
    ("coffee-shops", "Cafeterías y Tiendas de Té",
     "Agiliza el Servicio de Tu Cafetería",
     "Sistema POS optimizado para el ritmo de las cafeterías, con gestión de bebidas personalizadas y programas de lealtad.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/01e87f0da06975dc8b67700bd190f3b6d640ce89-1100x700.png",
     ["Modificadores de bebidas rápidos", "Programa de fidelidad integrado", "Pedidos anticipados por app", "Gestión de inventario de ingredientes", "Pantalla de preparación para baristas", "Reportes de artículos más vendidos"]),
    ("enterprise", "Cadenas y Multi-Ubicaciones",
     "Un Sistema para Gobernarlos a Todos",
     "Plataforma empresarial para gestionar múltiples restaurantes desde un panel centralizado con visibilidad completa.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/ff2922160f7797d6b0f6525bff2cbfc75e0b6e6e-1100x700.png",
     ["Dashboard centralizado multi-ubicación", "Sincronización de menú en todas las sucursales", "Reportes consolidados", "Gestión de usuarios y permisos", "API empresarial", "Implementación y soporte dedicado"]),
]

for slug, title, h2, sub, img, feats in rt_pages:
    feat_li = ''.join(f'<li>{f}</li>' for f in feats)
    body = page_hero(title, sub, "Tipos de Restaurantes") + f"""
<section class="bg-white section-pad">
  <div class="container">
    <div class="feature-split reveal">
      <div class="feature-text">
        <h2>{h2}</h2>
        <div class="orange-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;margin-bottom:1.5rem">{sub}</p>
        <ul class="feature-list">{feat_li}</ul>
        <a href="/skytab-espanol/contact.html" class="btn btn-primary">Obtener una Demo</a>
      </div>
      <div><img src="{img}" alt="{title}" style="border-radius:12px;width:100%"/></div>
    </div>
  </div>
</section>
""" + cta()
    page(title, sub, body, f"restaurant-types/{slug}.html")

print("✅ Restaurant type pages done")

# ─── HARDWARE SUB-PAGES ───────────────────────────────────────────────────────
hw_pages = [
    ("pos-system", "Sistema POS SkyTab",
     "El Corazón de Tu Operación",
     "Estación de trabajo potente y elegante diseñada para el entorno de restaurante más exigente.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/11f456621c4c1f710ca70d2e47017fdcfa6bc1ef-660x728.png",
     ["Pantalla táctil HD de 15.6\"", "Procesador de alta velocidad", "Software SkyTab preinstalado", "Garantía de por vida", "Diseño resistente a agua y polvo", "Instalación y configuración incluidas"]),
    ("handheld", "SkyTab Air — Terminal Portátil",
     "Toma Pedidos y Pagos en Cualquier Lugar",
     "Terminal portátil con batería de larga duración para tomar pedidos y procesar pagos en la mesa, terraza o delivery.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/c54506cb23720c00b8b18f401316f1478652d51c-660x728.png",
     ["Batería de 10+ horas", "Acepta chip, banda y NFC", "Pantalla táctil 5.5\"", "Resistente a caídas y salpicaduras", "Impresión de tickets integrada", "Sincronización en tiempo real con el POS"]),
    ("kiosk", "Quiosco de Autoservicio",
     "Deja que Tus Clientes Se Sirvan Solos",
     "Quiosco interactivo que permite a los clientes ordenar y pagar sin esperar. Aumenta el ticket promedio y reduce la presión sobre el personal.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/611f0e498abdaf16b56b10d01d89b31055c38aa8-1007x798.png",
     ["Pantalla táctil de 22\"", "Aceptación de tarjeta y efectivo", "Menú con fotos y videos", "Sugerencias automáticas de upsell", "Integración directa con cocina", "Modo de accesibilidad incluido"]),
    ("kitchen-display", "Pantalla de Cocina (KDS)",
     "Coordina Tu Cocina en Tiempo Real",
     "Pantalla de cocina digital resistente que muestra pedidos en tiempo real, mejora la comunicación y elimina el papel.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/52e29e564ee16f05790a418bffff59a37159fadd-1100x700.png",
     ["Pantalla industrial resistente al calor", "Pedidos organizados por prioridad", "Alertas de tiempo de preparación", "Múltiples estaciones de cocina", "Sincronización instantánea con el POS", "Reduce errores de comunicación"]),
    ("customer-display", "Pantalla para Clientes",
     "Transparencia y Confianza en el Mostrador",
     "Pantalla orientada al cliente que muestra el resumen del pedido, precios y opciones de propina.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/4db6a8fb18c277a1e30f20f4608903f405d36dec-1100x700.webp",
     ["Muestra resumen del pedido en tiempo real", "Opciones de propina sugeridas", "Aceptación de firma digital", "Imagen de marca personalizable", "Pantalla de 10.1\" HD", "Modo publicidad entre pedidos"]),
    ("accessories", "Accesorios POS",
     "Completa Tu Configuración",
     "Todo lo que necesitas para completar tu setup: impresoras, cajones de dinero, lectores de código de barras y más.",
     "https://cdn.sanity.io/images/2nz3tcxf/production/b2557e313b2e61b9afb85514f223a5c79af34007-1100x700.webp",
     ["Impresoras de recibos térmicas", "Cajones de dinero resistentes", "Lectores de código de barras", "Impresoras de etiquetas", "Soportes y montajes de pared", "Cables y conectividad"]),
]

for slug, title, h2, sub, img, feats in hw_pages:
    feat_li = ''.join(f'<li>{f}</li>' for f in feats)
    body = page_hero(title, sub, "Hardware POS") + f"""
<section class="bg-white section-pad">
  <div class="container">
    <div class="feature-split reveal">
      <div class="feature-text">
        <h2>{h2}</h2>
        <div class="orange-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;margin-bottom:1.5rem">{sub}</p>
        <ul class="feature-list">{feat_li}</ul>
        <a href="/skytab-espanol/contact.html" class="btn btn-primary">Solicitar Cotización</a>
      </div>
      <div><img src="{img}" alt="{title}" style="border-radius:12px;width:100%;max-width:420px;margin:0 auto;display:block"/></div>
    </div>
  </div>
</section>
""" + cta("¿Necesitas Ayuda para Elegir el Hardware?", "Nuestros especialistas te ayudarán a encontrar la configuración perfecta.")
    page(title, sub, body, f"pos-hardware/{slug}.html")

print("✅ Hardware pages done")
print(f"\n🎉 All pages generated in {BASE}/")
