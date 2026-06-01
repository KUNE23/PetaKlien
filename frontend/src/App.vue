<template>
  <DashboardPage v-if="currentPage === 'dashboard'" @back-home="currentPage = 'landing'" />
  <div v-else class="min-h-screen bg-background text-on-surface">
    <nav class="sticky top-0 z-50 border-b border-outline-variant/60 bg-surface/90 backdrop-blur">
      <div class="mx-auto flex h-20 max-w-container items-center justify-between px-4 sm:px-6 lg:px-10">
        <a class="flex items-center gap-3" href="#top" aria-label="PetaKlien">
          <span class="grid h-10 w-10 place-items-center rounded-lg bg-primary text-sm font-black text-white shadow-sm">PK</span>
          <span class="text-xl font-bold text-primary">PetaKlien</span>
        </a>

        <div class="hidden items-center gap-8 md:flex">
          <a v-for="item in navItems" :key="item.href" class="text-sm font-semibold text-on-surface-variant transition hover:text-primary" :href="item.href">
            {{ item.label }}
          </a>
        </div>

        <div class="flex items-center gap-2 sm:gap-3">
          <button class="hidden rounded-lg px-4 py-2 text-sm font-semibold text-on-surface-variant transition hover:text-primary sm:inline-flex" @click="currentPage = 'dashboard'">
            Dashboard
          </button>
          <button class="hidden rounded-lg px-4 py-2 text-sm font-semibold text-on-surface-variant transition hover:text-primary sm:inline-flex" @click="showLoginToast">
            Masuk
          </button>
          <button class="inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2.5 text-sm font-bold text-white shadow-lg shadow-primary/20 transition hover:bg-primary-strong sm:px-5" @click="showTrialToast">
            Coba Gratis
            <ArrowRight class="h-4 w-4" />
          </button>
        </div>
      </div>
    </nav>

    <main id="top">
      <section class="overflow-hidden py-16 sm:py-20 lg:py-24">
        <div class="mx-auto grid max-w-container grid-cols-1 items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.92fr_1.08fr] lg:gap-16 lg:px-10">
          <div>
            <span class="mb-6 inline-flex items-center gap-2 rounded-full bg-primary-fixed px-3 py-1 text-xs font-bold uppercase tracking-wide text-primary">
              <BadgeCheck class="h-4 w-4" />
              Lead generation berbasis lokasi
            </span>
            <h1 class="max-w-3xl text-4xl font-black leading-tight tracking-normal text-on-surface sm:text-5xl lg:text-[56px]">
              Temukan calon klien website dari Google Maps,
              <span class="text-primary">tanpa hunting manual.</span>
            </h1>
            <p class="mt-6 max-w-xl text-base leading-7 text-on-surface-variant">
              PetaKlien membantu freelancer, web studio, dan agency menemukan bisnis lokal yang belum punya website, menilai peluangnya, lalu menyimpan lead dalam dashboard yang rapi.
            </p>
            <div class="mt-9 flex flex-wrap gap-3">
              <button class="inline-flex items-center gap-2 rounded-lg bg-primary px-6 py-4 text-base font-bold text-white shadow-xl shadow-primary/20 transition hover:bg-primary-strong" @click="showSearchToast">
                Mulai Cari Lead
                <ArrowRight class="h-5 w-5" />
              </button>
              <a class="inline-flex items-center gap-2 rounded-lg border border-outline-variant bg-surface px-6 py-4 text-base font-bold text-on-surface transition hover:border-primary hover:text-primary" href="#how-it-works">
                Lihat Cara Kerja
              </a>
            </div>
          </div>

          <div class="relative">
            <div class="absolute inset-4 rounded-[32px] bg-primary/10 blur-3xl"></div>
            <div class="relative overflow-hidden rounded-xl border border-outline-variant bg-surface-container-lowest shadow-2xl">
              <div class="flex items-center justify-between border-b border-outline-variant bg-surface-container p-4">
                <div class="flex gap-2">
                  <span class="h-3 w-3 rounded-full bg-error"></span>
                  <span class="h-3 w-3 rounded-full bg-primary/30"></span>
                  <span class="h-3 w-3 rounded-full bg-success/40"></span>
                </div>
                <div class="hidden items-center gap-2 rounded-lg border border-outline-variant bg-white px-3 py-1 text-xs font-semibold text-on-surface-variant sm:flex">
                  <Search class="h-4 w-4" />
                  maps/search?q=laundry+jakarta
                </div>
              </div>

              <div class="grid min-h-[420px] grid-cols-1 sm:grid-cols-[270px_1fr]">
                <div class="border-b border-outline-variant bg-surface p-4 sm:border-b-0 sm:border-r">
                  <LeadPreview name="Kopi Senja Utama" score="9.1" status="Belum punya website" tone="danger" />
                  <LeadPreview name="Laundry Bersih 24h" score="8.4" status="Hanya Instagram" tone="primary" />
                  <LeadPreview name="Bakso Mang Udin" score="7.2" status="Website error" tone="warning" />
                </div>
                <div class="relative min-h-[320px] overflow-hidden bg-map-pattern">
                  <div class="absolute inset-0 bg-[linear-gradient(90deg,rgba(88,0,216,.12)_1px,transparent_1px),linear-gradient(rgba(88,0,216,.12)_1px,transparent_1px)] bg-[size:42px_42px]"></div>
                  <div class="absolute left-[18%] top-[26%] h-28 w-40 rounded-full border border-primary/20 bg-white/50 blur-sm"></div>
                  <div class="absolute right-[15%] top-[18%] h-36 w-48 rounded-full border border-success/20 bg-white/40 blur-sm"></div>
                  <MapPin class="absolute left-[52%] top-[48%] h-12 w-12 -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary p-2 text-white shadow-xl" />
                  <div class="absolute bottom-5 left-5 right-5 rounded-lg border border-white/70 bg-white/80 p-4 shadow-lg backdrop-blur">
                    <p class="text-xs font-bold uppercase tracking-wide text-primary">Radius 100 km</p>
                    <p class="mt-1 text-sm font-semibold text-on-surface">28 lead potensial ditemukan di Jakarta Selatan</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="bg-surface py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 text-center sm:px-6 lg:px-10">
          <h2 class="text-3xl font-black sm:text-4xl">Masalahnya bukan skill, tapi waktu.</h2>
          <p class="mx-auto mt-4 max-w-2xl text-on-surface-variant">
            Mencari klien website secara manual melelahkan, sulit diprioritaskan, dan datanya cepat berantakan.
          </p>
          <div class="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3">
            <ProblemCard :icon="Clock3" title="Manual search melelahkan" text="Browsing Google Maps satu per satu menghabiskan jam kerja yang bisa dipakai untuk closing atau produksi." tone="error" />
            <ProblemCard :icon="ListChecks" title="Lead tidak terprioritaskan" text="Semua bisnis terlihat sama sampai Anda tahu siapa yang belum punya website dan paling siap ditawarkan solusi." tone="primary" />
            <ProblemCard :icon="Rows3" title="Follow-up berantakan" text="PetaKlien menyatukan lead, status, skor, dan catatan agar pipeline tetap mudah dipantau." tone="tertiary" />
          </div>
        </div>
      </section>

      <section id="how-it-works" class="py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 sm:px-6 lg:px-10">
          <div class="text-center">
            <h2 class="text-3xl font-black sm:text-4xl">Alur Kerja PetaKlien</h2>
          </div>
          <div class="mt-12 grid grid-cols-1 gap-5 md:grid-cols-5">
            <WorkflowStep :icon="MapPinned" title="Maps Scan" text="Tentukan lokasi, radius, dan kategori bisnis." />
            <WorkflowStep :icon="SearchCheck" title="Website Check" text="Deteksi website, sosial media, dan kontak publik." />
            <WorkflowStep :icon="BarChart3" title="Scoring" text="Urutkan lead berdasarkan peluang proyek." />
            <WorkflowStep :icon="CheckCircle2" title="Approval" text="Pilih lead sebelum follow-up manual." />
            <WorkflowStep :icon="LayoutDashboard" title="Dashboard" text="Kelola status dan ekspor data." />
          </div>
        </div>
      </section>

      <section id="features" class="bg-surface-container-low py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 sm:px-6 lg:px-10">
          <h2 class="text-center text-3xl font-black sm:text-4xl">Fitur Utama untuk Keunggulan Anda</h2>
          <div class="mt-12 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            <FeatureCard :icon="Search" title="Pencarian Terarah" text="Cari bisnis berdasarkan kota, radius, dan kategori yang paling relevan dengan layanan Anda." />
            <FeatureCard :icon="Globe2" title="Deteksi Status Website" text="Bedakan bisnis yang belum punya website, hanya punya sosial media, atau sudah punya domain sendiri." />
            <FeatureCard :icon="TrendingUp" title="Skor Peluang" text="Prioritaskan lead berdasarkan website, kontak, kategori, Instagram, dan tanda bisnis aktif." />
            <FeatureCard :icon="ShieldCheck" title="Approval Workflow" text="Status default tetap draft. Follow-up tidak pernah dikirim otomatis oleh sistem." />
            <FeatureCard :icon="Database" title="Export Lokal" text="Hasil pencarian tetap berada di browser dan bisa diekspor ke CSV atau PDF tanpa campur data." />
            <FeatureCard :icon="Table2" title="Google Sheets Sync" text="Ekspor lead dan laporan ke spreadsheet untuk arsip atau kolaborasi tim." />
          </div>
        </div>
      </section>

      <section id="dashboard" class="py-16 sm:py-20">
        <div class="mx-auto grid max-w-container grid-cols-1 items-center gap-10 px-4 sm:px-6 lg:grid-cols-[0.85fr_1.15fr] lg:px-10">
          <div>
            <h2 class="text-3xl font-black sm:text-4xl">Kelola lead tanpa pusing</h2>
            <p class="mt-5 max-w-xl leading-7 text-on-surface-variant">
              Dashboard PetaKlien dirancang untuk kerja harian: lihat statistik, filter berdasarkan status website, cek kontak yang bisa dihubungi, lalu ubah status pipeline secara manual.
            </p>
            <div class="mt-8 grid gap-4">
              <MiniBenefit :icon="SlidersHorizontal" title="Filter cepat" text="Cari lead berdasarkan kota, kategori, status, dan peluang." />
              <MiniBenefit :icon="MousePointerClick" title="Aksi manual" text="Approve, skip, contacted, dan closed tetap di bawah kontrol pengguna." />
            </div>
          </div>

          <div class="overflow-hidden rounded-xl border border-outline-variant bg-white shadow-2xl">
            <div class="grid grid-cols-1 gap-4 border-b border-outline-variant p-5 sm:grid-cols-3">
              <StatCard label="Total Leads" value="128" tone="primary" />
              <StatCard label="No Website" value="42" tone="error" />
              <StatCard label="Potensi Tinggi" value="15" tone="success" />
            </div>
            <div class="overflow-x-auto p-5">
              <table class="w-full min-w-[560px] text-left">
                <thead>
                  <tr class="border-b border-outline-variant text-xs uppercase tracking-wide text-on-surface-variant">
                    <th class="pb-3">Nama Bisnis</th>
                    <th class="pb-3">Status Website</th>
                    <th class="pb-3">Skor</th>
                    <th class="pb-3">Aksi</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-outline-variant">
                  <DashboardRow name="Resto Sedap Malam" city="Jakarta Selatan" status="Belum ada" score="9.4" />
                  <DashboardRow name="Klinik Sehat Bersama" city="Depok" status="Hanya sosial media" score="8.8" />
                  <DashboardRow name="Laundry Prima 24 Jam" city="Bekasi" status="Belum ada" score="8.5" />
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>

      <section id="ethics" class="bg-surface-container-high/40 py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 text-center sm:px-6 lg:px-10">
          <h2 class="text-3xl font-black sm:text-4xl">Dibuat untuk follow-up yang etis</h2>
          <div class="mt-12 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
            <EthicCard :icon="ShieldCheck" title="Bukan Spam" text="PetaKlien tidak mengirim proposal otomatis ke email atau WhatsApp." />
            <EthicCard :icon="FileSearch" title="Data Publik" text="MVP memakai data sample dan siap diarahkan ke API resmi atau input CSV." />
            <EthicCard :icon="Handshake" title="Kemitraan" text="Fokus pada solusi website yang membantu bisnis lokal tampil profesional." />
            <EthicCard :icon="Lock" title="Privasi Terjaga" text="Credential disimpan di environment dan hasil pencarian tetap di browser user." />
          </div>
        </div>
      </section>

      <section class="py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 text-center sm:px-6 lg:px-10">
          <h2 class="text-3xl font-black sm:text-4xl">Siapa yang menggunakan PetaKlien?</h2>
          <div class="mt-12 grid grid-cols-2 gap-6 lg:grid-cols-4">
            <AudienceCard :icon="Code2" label="Freelance Devs" />
            <AudienceCard :icon="Megaphone" label="Agency Digital" />
            <AudienceCard :icon="Brush" label="Web Studio" />
            <AudienceCard :icon="Rocket" label="Jasa Digital" />
          </div>
        </div>
      </section>

      <section id="pricing" class="bg-surface py-16 sm:py-20">
        <div class="mx-auto max-w-container px-4 sm:px-6 lg:px-10">
          <h2 class="text-center text-3xl font-black sm:text-4xl">Pilih paket sesuai kebutuhan</h2>
          <div class="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3">
            <PricingCard name="Starter" price="Rp 199k" text="Cocok untuk freelance pemula." :check-icon="Check" :features="['100 search credits / bulan', 'Auto-detect website', 'Leads dashboard']" />
            <PricingCard featured name="Pro" price="Rp 499k" text="Untuk yang serius ingin closing." :check-icon="Check" :features="['1.000 search credits / bulan', 'Lead opportunity scoring', 'Google Sheets export', 'Approval workflow']" />
            <PricingCard name="Agency" price="Rp 999k" text="Skala besar untuk tim agency." :check-icon="Check" :features="['Unlimited search credits', 'Multi-user access', 'API access', 'Priority support']" />
          </div>
        </div>
      </section>

      <section class="bg-primary py-16 text-center text-white sm:py-20">
        <div class="mx-auto max-w-4xl px-4 sm:px-6">
          <h2 class="text-4xl font-black leading-tight sm:text-5xl">Dari peta ke klien, tanpa manual tanpa capek.</h2>
          <p class="mx-auto mt-5 max-w-2xl text-primary-soft">
            Mulai dari dashboard internal, lalu kembangkan menjadi portfolio SaaS yang menunjukkan kemampuan backend, database, dan frontend Anda.
          </p>
          <button class="mt-9 rounded-lg bg-white px-8 py-4 text-base font-black text-primary shadow-xl transition hover:bg-primary-fixed" @click="showTrialToast">
            Mulai Uji Coba Gratis 7 Hari
          </button>
        </div>
      </section>
    </main>

    <footer class="border-t border-outline-variant bg-surface-container-low py-12">
      <div class="mx-auto grid max-w-container grid-cols-1 gap-8 px-4 sm:px-6 md:grid-cols-4 lg:px-10">
        <div class="md:col-span-2">
          <div class="flex items-center gap-3">
            <span class="grid h-9 w-9 place-items-center rounded-lg bg-primary text-xs font-black text-white">PK</span>
            <span class="text-lg font-black text-primary">PetaKlien</span>
          </div>
          <p class="mt-4 max-w-md text-sm leading-6 text-on-surface-variant">
            Platform lead discovery berbasis lokasi untuk membantu developer dan agency menemukan peluang website secara lebih terstruktur.
          </p>
        </div>
        <FooterLinks title="Navigasi" :items="['Fitur', 'Cara Kerja', 'Dashboard', 'Harga']" />
        <FooterLinks title="Bantuan" :items="['Dokumentasi', 'Tutorial', 'Kontak']" />
      </div>
      <div class="mx-auto mt-10 max-w-container border-t border-outline-variant px-4 pt-6 text-sm text-on-surface-variant sm:px-6 lg:px-10">
        © 2026 PetaKlien. Follow-up tetap manual dan etis.
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useToast } from 'vue-toastification'
import DashboardPage from './DashboardPage.vue'
import {
  ArrowRight,
  BadgeCheck,
  BarChart3,
  Brush,
  Check,
  CheckCircle2,
  Clock3,
  Code2,
  Database,
  FileSearch,
  Globe2,
  Handshake,
  LayoutDashboard,
  ListChecks,
  Lock,
  MapPin,
  MapPinned,
  Megaphone,
  MousePointerClick,
  Rocket,
  Rows3,
  Search,
  SearchCheck,
  ShieldCheck,
  SlidersHorizontal,
  Table2,
  TrendingUp,
} from '@lucide/vue'

const toast = useToast()
const currentPage = ref('landing')

const navItems = [
  { label: 'Fitur', href: '#features' },
  { label: 'Cara Kerja', href: '#how-it-works' },
  { label: 'Dashboard', href: '#dashboard' },
  { label: 'Etika', href: '#ethics' },
  { label: 'Harga', href: '#pricing' },
]

function showTrialToast() {
  toast.success('CTA siap. Hubungkan tombol ini ke halaman registrasi saat auth sudah dibuat.')
}

function showLoginToast() {
  toast.info('Halaman login belum diaktifkan di landing page ini.')
}

function showSearchToast() {
  currentPage.value = 'dashboard'
  toast.info('Dashboard pencarian dibuka.')
}
</script>

<script>
export default {
  components: {
    LeadPreview: {
      props: ['name', 'score', 'status', 'tone'],
      computed: {
        toneClass() {
          return {
            danger: 'text-error bg-error/10',
            primary: 'text-primary bg-primary/10',
            warning: 'text-amber-700 bg-amber-100',
          }[this.tone]
        },
      },
      template: `
        <div class="mb-3 rounded-lg border border-outline-variant bg-white p-3 shadow-sm first:border-primary">
          <div class="mb-1 flex items-start justify-between gap-3">
            <span class="text-sm font-black leading-tight">{{ name }}</span>
            <span class="rounded bg-primary-fixed px-2 py-0.5 text-xs font-black text-primary">{{ score }}</span>
          </div>
          <span class="inline-flex rounded-full px-2 py-1 text-xs font-bold" :class="toneClass">{{ status }}</span>
        </div>
      `,
    },
    ProblemCard: {
      props: ['icon', 'title', 'text', 'tone'],
      computed: {
        toneClass() {
          return {
            error: 'bg-error/10 text-error',
            primary: 'bg-primary-fixed text-primary',
            tertiary: 'bg-tertiary/10 text-tertiary',
          }[this.tone]
        },
      },
      template: `
        <article class="rounded-lg border border-outline-variant bg-white p-7 text-left shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
          <div class="mb-5 grid h-12 w-12 place-items-center rounded-lg" :class="toneClass">
            <component :is="icon" class="h-6 w-6" />
          </div>
          <h3 class="text-lg font-black">{{ title }}</h3>
          <p class="mt-3 text-sm leading-6 text-on-surface-variant">{{ text }}</p>
        </article>
      `,
    },
    WorkflowStep: {
      props: ['icon', 'title', 'text'],
      template: `
        <article class="rounded-lg bg-background p-5 text-center">
          <div class="mx-auto mb-5 grid h-16 w-16 place-items-center rounded-full bg-primary text-white shadow-lg ring-8 ring-background">
            <component :is="icon" class="h-7 w-7" />
          </div>
          <h3 class="font-black">{{ title }}</h3>
          <p class="mt-2 text-sm leading-5 text-on-surface-variant">{{ text }}</p>
        </article>
      `,
    },
    FeatureCard: {
      props: ['icon', 'title', 'text'],
      template: `
        <article class="rounded-lg border border-outline-variant bg-white p-7 transition hover:border-primary hover:shadow-lg">
          <component :is="icon" class="mb-5 h-8 w-8 text-primary" />
          <h3 class="text-lg font-black">{{ title }}</h3>
          <p class="mt-3 text-sm leading-6 text-on-surface-variant">{{ text }}</p>
        </article>
      `,
    },
    MiniBenefit: {
      props: ['icon', 'title', 'text'],
      template: `
        <div class="flex items-start gap-4">
          <div class="grid h-12 w-12 shrink-0 place-items-center rounded-lg bg-primary/10 text-primary">
            <component :is="icon" class="h-6 w-6" />
          </div>
          <div>
            <h3 class="font-black">{{ title }}</h3>
            <p class="mt-1 text-sm text-on-surface-variant">{{ text }}</p>
          </div>
        </div>
      `,
    },
    StatCard: {
      props: ['label', 'value', 'tone'],
      computed: {
        cardClass() {
          return {
            primary: 'bg-primary/5 text-primary border-primary/10',
            error: 'bg-error/5 text-error border-error/10',
            success: 'bg-success/5 text-success border-success/10',
          }[this.tone]
        },
      },
      template: `
        <div class="rounded-lg border p-5" :class="cardClass">
          <span class="text-xs font-black uppercase tracking-wide text-on-surface-variant">{{ label }}</span>
          <p class="mt-1 text-3xl font-black">{{ value }}</p>
        </div>
      `,
    },
    DashboardRow: {
      props: ['name', 'city', 'status', 'score'],
      template: `
        <tr>
          <td class="py-4">
            <div class="text-sm font-black">{{ name }}</div>
            <div class="mt-1 text-xs text-on-surface-variant">{{ city }}</div>
          </td>
          <td class="py-4">
            <span class="rounded-full bg-primary-fixed px-3 py-1 text-xs font-black text-primary">{{ status }}</span>
          </td>
          <td class="py-4 text-sm font-black text-success">{{ score }}</td>
          <td class="py-4">
            <button class="rounded-lg bg-primary px-3 py-1.5 text-xs font-black text-white">Follow Up</button>
          </td>
        </tr>
      `,
    },
    EthicCard: {
      props: ['icon', 'title', 'text'],
      template: `
        <article class="rounded-lg bg-white p-6 shadow-sm">
          <component :is="icon" class="mx-auto mb-4 h-7 w-7 text-primary" />
          <h3 class="font-black">{{ title }}</h3>
          <p class="mt-2 text-sm leading-5 text-on-surface-variant">{{ text }}</p>
        </article>
      `,
    },
    AudienceCard: {
      props: ['icon', 'label'],
      template: `
        <article class="flex flex-col items-center">
          <div class="grid h-24 w-24 place-items-center rounded-full bg-primary/10 text-primary">
            <component :is="icon" class="h-10 w-10" />
          </div>
          <span class="mt-4 text-lg font-black">{{ label }}</span>
        </article>
      `,
    },
    PricingCard: {
      props: ['name', 'price', 'text', 'features', 'featured', 'checkIcon'],
      template: `
        <article class="relative flex rounded-xl border bg-white p-8 shadow-sm transition hover:shadow-xl" :class="featured ? 'scale-[1.02] border-2 border-primary shadow-xl' : 'border-outline-variant'">
          <div v-if="featured" class="absolute left-1/2 top-0 -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary px-4 py-1 text-xs font-black text-white">POPULER</div>
          <div class="flex w-full flex-col">
            <h3 class="text-xl font-black">{{ name }}</h3>
            <p class="mt-2 text-sm text-on-surface-variant">{{ text }}</p>
            <div class="mt-7">
              <span class="text-3xl font-black">{{ price }}</span>
              <span class="text-on-surface-variant">/bln</span>
            </div>
            <ul class="mt-8 grid flex-1 gap-4 text-sm">
              <li v-for="feature in features" :key="feature" class="flex items-center gap-2">
                <component :is="checkIcon" class="h-5 w-5 text-success" />
                {{ feature }}
              </li>
            </ul>
            <button class="mt-9 rounded-lg px-4 py-3 font-black transition" :class="featured ? 'bg-primary text-white hover:bg-primary-strong' : 'border border-primary text-primary hover:bg-primary-fixed'">
              {{ featured ? 'Langganan Sekarang' : 'Pilih Paket' }}
            </button>
          </div>
        </article>
      `,
    },
    FooterLinks: {
      props: ['title', 'items'],
      template: `
        <div>
          <h3 class="font-black">{{ title }}</h3>
          <ul class="mt-4 grid gap-3 text-sm text-on-surface-variant">
            <li v-for="item in items" :key="item"><a class="transition hover:text-primary hover:underline" href="#top">{{ item }}</a></li>
          </ul>
        </div>
      `,
    },
  },
}
</script>
