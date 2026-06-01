<template>
  <div class="min-h-screen bg-background text-on-surface">
    <header class="sticky top-0 z-50 border-b border-outline-variant bg-surface/90 shadow-sm backdrop-blur">
      <div class="mx-auto flex h-20 max-w-container items-center justify-between px-4 sm:px-6 lg:px-10">
        <div class="flex items-center gap-8">
          <button class="text-2xl font-black text-primary" @click="$emit('back-home')">PetaKlien</button>
          <nav class="hidden items-center gap-6 md:flex">
            <button
              v-for="item in navItems"
              :key="item"
              class="border-b-2 pb-1 text-xs font-bold uppercase tracking-wide transition"
              :class="item === activeNav ? 'border-primary text-primary' : 'border-transparent text-on-surface-variant hover:text-primary'"
              @click="activeNav = item"
            >
              {{ item }}
            </button>
          </nav>
        </div>

        <div class="flex items-center gap-3">
          <button class="hidden rounded-lg bg-primary px-5 py-2.5 text-sm font-bold text-white transition hover:bg-primary-strong sm:inline-flex" @click="toast.info('Upgrade plan belum diaktifkan.')">
            Upgrade
          </button>
          <button class="rounded-full p-2 text-on-surface-variant transition hover:bg-surface-container" aria-label="Notifikasi" @click="toast.info('Tidak ada notifikasi baru.')">
            <Bell class="h-5 w-5" />
          </button>
          <div class="grid h-10 w-10 place-items-center overflow-hidden rounded-full border border-outline-variant bg-surface-container-high text-sm font-black text-primary">
            AK
          </div>
        </div>
      </div>
    </header>

    <main class="mx-auto grid max-w-container grid-cols-12 gap-6 px-4 py-8 sm:px-6 lg:px-10">
      <section class="col-span-12">
        <div class="flex flex-col gap-3">
          <div class="flex flex-wrap items-center gap-3">
            <h1 class="text-3xl font-black leading-tight sm:text-4xl">Dashboard Lead Finder</h1>
            <span class="inline-flex items-center gap-1 rounded-full border border-emerald-200 bg-emerald-100 px-3 py-1 text-xs font-black text-emerald-700">
              <CheckCircle2 class="h-4 w-4 fill-emerald-600 text-emerald-600" />
              Lead Finder Active
            </span>
          </div>
          <p class="max-w-2xl leading-7 text-on-surface-variant">
            Cari bisnis lokal yang belum memiliki website dan kelola prospeknya dengan lebih cepat menggunakan intelijen data geografis.
          </p>
        </div>
      </section>

      <section class="col-span-12 flex flex-col gap-8 lg:col-span-8">
        <article class="overflow-hidden rounded-xl border border-outline-variant bg-white shadow-sm">
          <div class="flex flex-col gap-4 border-b border-outline-variant p-5 sm:flex-row sm:items-center sm:justify-between">
            <h2 class="text-xl font-black">Cari Lead Baru</h2>
            <div class="grid grid-cols-2 rounded-lg bg-surface-container-low p-1">
              <button class="rounded-md px-4 py-2 text-sm font-bold transition" :class="activeTab === 'manual' ? 'bg-white text-primary shadow-sm' : 'text-on-surface-variant'" @click="activeTab = 'manual'">
                Input Manual
              </button>
              <button class="rounded-md px-4 py-2 text-sm font-bold transition" :class="activeTab === 'maps' ? 'bg-white text-primary shadow-sm' : 'text-on-surface-variant'" @click="activeTab = 'maps'">
                Cari dari Peta
              </button>
            </div>
          </div>

          <form v-if="activeTab === 'manual'" class="grid gap-6 p-5 sm:p-8" @submit.prevent="searchLeads">
            <div class="grid gap-4 md:grid-cols-2">
              <label class="grid gap-2 text-xs font-black uppercase tracking-wide text-on-surface-variant">
                Kota
                <input v-model="form.city" class="rounded-xl border border-outline-variant px-4 py-3 text-base font-medium normal-case tracking-normal text-on-surface outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20" placeholder="Contoh: Tasikmalaya" type="text" />
              </label>
              <label class="grid gap-2 text-xs font-black uppercase tracking-wide text-on-surface-variant">
                Negara
                <select v-model="form.country" class="rounded-xl border border-outline-variant px-4 py-3 text-base font-medium normal-case tracking-normal text-on-surface outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20">
                  <option>Indonesia</option>
                  <option>Malaysia</option>
                  <option>Singapore</option>
                </select>
              </label>
            </div>
            <div class="grid gap-4 md:grid-cols-2">
              <label class="grid gap-2 text-xs font-black uppercase tracking-wide text-on-surface-variant">
                Kategori Bisnis
                <select v-model="form.category" class="rounded-xl border border-outline-variant px-4 py-3 text-base font-medium normal-case tracking-normal text-on-surface outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20">
                  <option value="cafe">Cafe</option>
                  <option value="restoran">Restoran</option>
                  <option value="laundry">Laundry</option>
                  <option value="barbershop">Barbershop</option>
                  <option value="bengkel">Bengkel</option>
                  <option value="toko">Toko</option>
                  <option value="klinik kecil">Klinik Kecil</option>
                  <option value="sekolah kecil">Sekolah Kecil</option>
                </select>
              </label>
              <label class="grid gap-2 text-xs font-black uppercase tracking-wide text-on-surface-variant">
                Jumlah Lead
                <input v-model.number="form.limit" class="rounded-xl border border-outline-variant px-4 py-3 text-base font-medium normal-case tracking-normal text-on-surface outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20" min="1" max="100" placeholder="Maks 100" type="number" />
              </label>
            </div>
            <label class="flex items-center gap-3 text-sm font-semibold text-on-surface">
              <input v-model="form.noWebsiteOnly" class="h-5 w-5 rounded border-outline-variant text-primary accent-primary" type="checkbox" />
              Hanya tampilkan bisnis yang belum punya website
            </label>
            <button class="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-primary px-5 py-4 font-black text-white shadow-md transition hover:bg-primary-strong disabled:cursor-progress disabled:opacity-70" type="submit" :disabled="loadingSearch">
              <Search class="h-5 w-5" />
              {{ loadingSearch ? 'Mencari...' : 'Mulai Cari' }}
            </button>
          </form>

          <div v-else class="grid gap-4 p-5 sm:p-8">
            <div class="relative h-[420px] overflow-hidden rounded-xl border border-outline-variant bg-map-pattern">
              <div class="absolute inset-0 bg-[linear-gradient(90deg,rgba(88,0,216,.12)_1px,transparent_1px),linear-gradient(rgba(88,0,216,.12)_1px,transparent_1px)] bg-[size:44px_44px]"></div>
              <MapPin class="absolute left-1/2 top-1/2 z-10 h-11 w-11 -translate-x-1/2 -translate-y-1/2 fill-primary text-primary drop-shadow-xl" />
              <MapPin class="absolute left-1/4 top-1/3 z-10 h-8 w-8 fill-primary text-primary drop-shadow-lg" />
              <MapPin class="absolute bottom-1/4 right-1/3 z-10 h-8 w-8 fill-primary text-primary drop-shadow-lg" />

              <div class="absolute left-4 right-4 top-4 z-20 flex gap-2">
                <div class="relative flex-1">
                  <Target class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-on-surface-variant" />
                  <input class="w-full rounded-xl border-0 bg-white/90 py-2 pl-10 pr-4 text-sm shadow-lg outline-none backdrop-blur focus:ring-2 focus:ring-primary" placeholder="Cari area di peta..." type="text" />
                </div>
                <div class="flex rounded-xl border border-outline-variant bg-white/90 p-1 shadow-lg backdrop-blur">
                  <button class="rounded-lg p-2 hover:bg-surface-container" type="button" @click="toast.info('Zoom in peta demo.')"><ZoomIn class="h-5 w-5" /></button>
                  <button class="rounded-lg p-2 hover:bg-surface-container" type="button" @click="toast.info('Zoom out peta demo.')"><ZoomOut class="h-5 w-5" /></button>
                </div>
              </div>

              <div class="absolute bottom-4 left-4 z-20 w-52 rounded-xl border border-outline-variant bg-white/90 p-4 shadow-lg backdrop-blur">
                <label class="mb-2 block text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Radius Pencarian</label>
                <input v-model="form.radius" class="w-full accent-primary" min="1" max="100" type="range" />
                <div class="mt-1 flex justify-between text-[10px] font-black">
                  <span>1 km</span>
                  <span>{{ form.radius }} km</span>
                </div>
              </div>
            </div>
            <button class="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-primary px-5 py-4 font-black text-white shadow-md transition hover:bg-primary-strong disabled:cursor-progress disabled:opacity-70" type="button" :disabled="loadingSearch" @click="searchFromMap">
              <Map class="h-5 w-5" />
              {{ loadingSearch ? 'Mengambil...' : 'Ambil Lead dari Peta' }}
            </button>
          </div>
        </article>

        <section class="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
          <MetricCard label="Total Lead" :value="String(stats.total)" :helper="`${stats.today} hari ini`" helper-class="text-emerald-600" />
          <MetricCard label="No Website" :value="String(stats.no_website)" :helper="noWebsitePercent" helper-class="text-error" />
          <MetricCard label="Hanya Sosmed" :value="String(stats.social_only)" :helper="socialOnlyPercent" helper-class="text-on-surface-variant" />
          <MetricCard label="Rata-rata Skor" :value="averageScore" helper="★" featured />
        </section>

        <article class="mb-10 overflow-hidden rounded-xl border border-outline-variant bg-white shadow-sm">
          <div class="space-y-4 border-b border-outline-variant p-5">
            <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <h2 class="text-xl font-black">Daftar Lead</h2>
              <div class="flex flex-wrap gap-2">
                <button class="rounded-lg px-4 py-2 text-sm font-bold text-on-surface-variant transition hover:bg-surface-container" @click="resetFilters">Reset Filter</button>
                <button class="inline-flex items-center gap-2 rounded-lg border border-outline-variant bg-surface-container-high px-4 py-2 text-sm font-bold text-on-surface transition hover:bg-surface-container" @click="exportCsv">
                  <Download class="h-4 w-4" />
                  Export CSV
                </button>
                <button class="inline-flex items-center gap-2 rounded-lg border border-outline-variant bg-surface-container-high px-4 py-2 text-sm font-bold text-on-surface transition hover:bg-surface-container" @click="exportPdf">
                  <FileDown class="h-4 w-4" />
                  Export PDF
                </button>
              </div>
            </div>
            <div class="grid grid-cols-1 gap-3 md:grid-cols-12">
              <div class="relative md:col-span-4">
                <Search class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-on-surface-variant" />
                <input v-model="filters.q" class="w-full rounded-lg border border-outline-variant py-2 pl-9 pr-4 text-sm outline-none focus:ring-2 focus:ring-primary/20" placeholder="Cari nama bisnis..." type="text" />
              </div>
              <select v-model="filters.website" class="rounded-lg border border-outline-variant px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/20 md:col-span-2">
                <option>Semua Status Web</option>
                <option>Belum ada</option>
                <option>Hanya sosial media</option>
                <option>Punya website</option>
              </select>
              <select v-model="filters.category" class="rounded-lg border border-outline-variant px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/20 md:col-span-2">
                <option>Kategori</option>
                <option v-for="category in categoryOptions" :key="category">{{ category }}</option>
              </select>
              <select v-model="filters.city" class="rounded-lg border border-outline-variant px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/20 md:col-span-2">
                <option>Kota</option>
                <option v-for="city in cityOptions" :key="city">{{ city }}</option>
              </select>
              <select v-model="filters.leadStatus" class="rounded-lg border border-outline-variant px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/20 md:col-span-2">
                <option>Status Lead</option>
                <option value="draft">Draft</option>
                <option value="approved">Approved</option>
                <option value="skipped">Skipped</option>
                <option value="contacted">Contacted</option>
                <option value="closed">Closed</option>
              </select>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full min-w-[860px] border-collapse text-left">
              <thead class="border-b border-outline-variant bg-surface-container-low">
                <tr>
                  <th class="p-4 text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Bisnis & Lokasi</th>
                  <th class="p-4 text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Kontak</th>
                  <th class="p-4 text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Status Web</th>
                  <th class="p-4 text-center text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Skor</th>
                  <th class="p-4 text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Status Lead</th>
                  <th class="p-4 text-right text-[10px] font-black uppercase tracking-widest text-on-surface-variant">Aksi</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-outline-variant/60">
                <tr v-for="lead in filteredLeads" :key="lead.id" class="transition hover:bg-surface-container-low/60">
                  <td class="p-4">
                    <div class="flex flex-col">
                      <span class="font-black text-on-surface">{{ lead.nama_bisnis }}</span>
                      <span class="text-xs text-on-surface-variant">{{ lead.kategori || '-' }} • {{ lead.kota || '-' }}, ID</span>
                    </div>
                  </td>
                  <td class="p-4">
                    <div class="flex items-center gap-2">
                      <component :is="contactIcon(lead)" class="h-4 w-4 text-primary" />
                      <span class="text-xs font-semibold text-on-surface-variant">{{ lead.kontak_bisa_dihubungi || lead.kontak || lead.email || lead.instagram || '-' }}</span>
                    </div>
                  </td>
                  <td class="p-4">
                    <span class="rounded px-2 py-1 text-[10px] font-black uppercase" :class="websiteBadgeClass(lead.status_website)">
                      {{ lead.status_website || '-' }}
                    </span>
                  </td>
                  <td class="p-4 text-center">
                    <span class="rounded-lg bg-primary/10 p-1.5 text-sm font-black text-primary">{{ lead.skor_peluang || 1 }}</span>
                  </td>
                  <td class="p-4">
                    <span class="inline-flex items-center gap-1 text-xs font-bold" :class="lead.status === 'approved' ? 'text-emerald-600' : 'text-on-surface-variant'">
                      <span class="h-2 w-2 rounded-full" :class="lead.status === 'approved' ? 'bg-emerald-500' : 'bg-slate-300'"></span>
                      {{ formatStatus(lead.status) }}
                    </span>
                  </td>
                  <td class="p-4 text-right">
                    <div class="flex justify-end gap-2">
                      <button class="rounded-lg p-2 text-primary transition hover:bg-primary/5" @click="openMaps(lead)"><Map class="h-4 w-4" /></button>
                      <button
                        class="rounded-lg px-3 py-1 text-xs font-black transition"
                        :class="lead.status === 'approved' ? 'cursor-not-allowed bg-surface-container-high text-on-surface-variant' : 'bg-primary text-white hover:bg-primary-strong'"
                        :disabled="lead.status === 'approved'"
                        @click="approveLead(lead)"
                      >
                        {{ lead.status === 'approved' ? 'Approved' : 'Approve' }}
                      </button>
                      <button class="rounded-lg p-2 text-on-surface-variant transition hover:bg-surface-container" @click="skipLead(lead)"><X class="h-4 w-4" /></button>
                    </div>
                  </td>
                </tr>
                <tr v-if="!filteredLeads.length">
                  <td class="p-8 text-center text-sm font-semibold text-on-surface-variant" colspan="6">
                    {{ loadingSearch ? 'Memuat data lead...' : 'Belum ada lead sesuai filter.' }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="flex flex-col gap-3 border-t border-outline-variant bg-surface-container-low p-4 sm:flex-row sm:items-center sm:justify-between">
            <span class="text-xs text-on-surface-variant">Menampilkan <span class="font-black text-on-surface">1-{{ filteredLeads.length }}</span> dari <span class="font-black text-on-surface">{{ stats.total }}</span> lead</span>
            <div class="flex items-center gap-3">
              <div class="hidden items-center gap-2 sm:flex">
                <span class="text-xs text-on-surface-variant">Baris per halaman:</span>
                <select class="bg-transparent p-0 text-xs font-black outline-none">
                  <option>10</option>
                  <option>25</option>
                  <option>50</option>
                </select>
              </div>
              <div class="flex gap-1">
                <button class="rounded-md p-1 hover:bg-surface-container"><ChevronLeft class="h-4 w-4" /></button>
                <button class="grid h-6 w-6 place-items-center rounded-md bg-primary text-xs font-black text-white">1</button>
                <button class="grid h-6 w-6 place-items-center rounded-md text-xs font-black text-on-surface-variant hover:bg-surface-container">2</button>
                <button class="grid h-6 w-6 place-items-center rounded-md text-xs font-black text-on-surface-variant hover:bg-surface-container">3</button>
                <button class="rounded-md p-1 hover:bg-surface-container"><ChevronRight class="h-4 w-4" /></button>
              </div>
            </div>
          </div>
        </article>
      </section>

      <aside class="col-span-12 flex flex-col gap-6 lg:col-span-4">
        <section class="rounded-xl border border-outline-variant bg-white p-5 shadow-sm lg:sticky lg:top-24">
          <div class="mb-6 flex items-center justify-between">
            <h2 class="inline-flex items-center gap-2 text-xl font-black">
              <Bolt class="h-6 w-6 fill-primary text-primary" />
              Lead Prioritas
            </h2>
            <span class="rounded bg-primary/10 px-2 py-0.5 text-[10px] font-black text-primary">HARI INI</span>
          </div>

          <div class="grid gap-4">
            <PriorityLead v-for="lead in priorityLeads" :key="lead.id || lead.nama_bisnis" :lead="lead" :eye-icon="Eye" @save="savePriorityLead" @view="viewPriorityLead" />
          </div>

          <button class="mt-6 w-full rounded-xl border border-dashed border-outline px-4 py-3 text-xs font-black text-on-surface-variant transition hover:bg-surface-container-low" @click="toast.info('Menampilkan semua rekomendasi prioritas.')">
            Lihat Semua Rekomendasi
          </button>
        </section>

        <section class="relative overflow-hidden rounded-xl bg-secondary p-6 text-white shadow-lg">
          <div class="relative z-10">
            <Lightbulb class="mb-3 h-6 w-6" />
            <h2 class="text-lg font-black leading-tight">Tips Lead Gen</h2>
            <p class="mt-2 text-xs leading-6 text-white/90">
              Fokus pada bisnis dengan skor di atas 9.0. Mereka biasanya memiliki ulasan Google Maps yang banyak namun belum memiliki digital presence yang baik.
            </p>
          </div>
          <ChartNoAxesCombined class="absolute -bottom-6 -right-6 h-32 w-32 text-white/10" />
        </section>
      </aside>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useToast } from 'vue-toastification'
import jsPDF from 'jspdf'
import autoTable from 'jspdf-autotable'
import {
  Bell,
  Bolt,
  ChartNoAxesCombined,
  CheckCircle2,
  ChevronLeft,
  ChevronRight,
  Download,
  FileDown,
  Eye,
  Globe2,
  Lightbulb,
  Map,
  MapPin,
  MessageCircle,
  Phone,
  Search,
  Target,
  X,
  ZoomIn,
  ZoomOut,
} from '@lucide/vue'

defineEmits(['back-home'])

const toast = useToast()
const activeNav = ref('Dashboard')
const activeTab = ref('manual')
const navItems = ['Dashboard', 'Leads', 'Approved', 'Reports', 'Settings']
const loadingSearch = ref(false)

const form = reactive({
  city: 'Tasikmalaya',
  country: 'Indonesia',
  category: 'cafe',
  limit: 20,
  noWebsiteOnly: true,
  radius: 5,
})

const filters = reactive({
  q: '',
  website: 'Semua Status Web',
  category: 'Kategori',
  city: 'Kota',
  leadStatus: 'Status Lead',
})

const stats = reactive({ total: 0, today: 0, draft: 0, approved: 0, no_website: 0, social_only: 0, returned: 0 })
const leads = ref([])

const categoryOptions = computed(() => [...new Set(leads.value.map((lead) => lead.kategori).filter(Boolean))])
const cityOptions = computed(() => [...new Set(leads.value.map((lead) => lead.kota).filter(Boolean))])
const priorityLeads = computed(() =>
  [...leads.value]
    .sort((a, b) => Number(b.skor_peluang || 0) - Number(a.skor_peluang || 0))
    .slice(0, 3)
    .map((lead, index) => ({ ...lead, highlighted: index === 0 }))
)

const filteredLeads = computed(() => {
  return leads.value.filter((lead) => {
    const query = filters.q.toLowerCase()
    const queryMatch =
      !query ||
      String(lead.nama_bisnis || '').toLowerCase().includes(query) ||
      String(lead.kategori || '').toLowerCase().includes(query) ||
      String(lead.kota || '').toLowerCase().includes(query)
    const websiteMatch = filters.website === 'Semua Status Web' || lead.status_website === filters.website
    const categoryMatch = filters.category === 'Kategori' || lead.kategori === filters.category
    const cityMatch = filters.city === 'Kota' || lead.kota === filters.city
    const statusMatch = filters.leadStatus === 'Status Lead' || lead.status === filters.leadStatus
    return queryMatch && websiteMatch && categoryMatch && cityMatch && statusMatch
  })
})

const noWebsitePercent = computed(() => percentage(stats.no_website, stats.total))
const socialOnlyPercent = computed(() => percentage(stats.social_only, stats.total))
const averageScore = computed(() => {
  if (!leads.value.length) return '0.0'
  const total = leads.value.reduce((sum, lead) => sum + Number(lead.skor_peluang || 0), 0)
  return (total / leads.value.length).toFixed(1)
})

watch(
  () => activeNav.value,
  (value) => {
    if (value === 'Approved') filters.leadStatus = 'approved'
    if (value === 'Leads' || value === 'Dashboard') filters.leadStatus = 'Status Lead'
  }
)

onMounted(async () => {
  await loadConfig()
})

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  })
  const data = await response.json()
  if (!response.ok) throw new Error(data.error || 'Request API gagal.')
  return data
}

async function loadConfig() {
  try {
    const data = await api('/api/config')
    form.city = data.default_city || form.city
    form.radius = data.default_radius_km || form.radius
    form.category = data.default_categories?.[0] || form.category
  } catch (error) {
    toast.error(error.message)
  }
}

async function searchLeads() {
  if (!form.city.trim()) {
    toast.error('Isi kota terlebih dahulu.')
    return
  }
  loadingSearch.value = true
  try {
    const data = await api('/api/find-public', {
      method: 'POST',
      body: JSON.stringify({
        city: form.city,
        categories: [form.category],
        radius_km: Number(form.radius || 100),
        limit: Number(form.limit || 20),
        no_website_only: Boolean(form.noWebsiteOnly),
      }),
    })
    const result = data.result || {}
    leads.value = data.leads || result.leads || []
    Object.assign(stats, {
      total: result.total ?? leads.value.length,
      today: result.total ?? leads.value.length,
      draft: leads.value.filter((lead) => lead.status === 'draft').length,
      approved: leads.value.filter((lead) => lead.status === 'approved').length,
      no_website: leads.value.filter((lead) => lead.status_website === 'Belum ada').length,
      social_only: leads.value.filter((lead) => lead.status_website === 'Hanya sosial media').length,
      returned: result.returned ?? leads.value.length,
    })
    toast.success(`Lead ditemukan: ${result.found || 0}, valid: ${result.valid || 0}, belum punya website: ${result.no_website || 0}.`)
  } catch (error) {
    toast.error(error.message)
  } finally {
    loadingSearch.value = false
  }
}

async function searchFromMap() {
  await searchLeads()
}

function changeLeadStatus(lead, status) {
  lead.status = status
  toast.success(`${lead.nama_bisnis} diubah ke ${formatStatus(status)}.`)
}

function approveLead(lead) {
  changeLeadStatus(lead, 'approved')
}

function skipLead(lead) {
  changeLeadStatus(lead, 'skipped')
}

function resetFilters() {
  filters.q = ''
  filters.website = 'Semua Status Web'
  filters.category = 'Kategori'
  filters.city = 'Kota'
  filters.leadStatus = 'Status Lead'
  toast.info('Filter lead direset.')
}

function websiteBadgeClass(status) {
  if (status === 'Belum ada') return 'bg-red-100 text-red-700'
  if (status === 'Hanya sosial media') return 'bg-orange-100 text-orange-700'
  return 'bg-emerald-100 text-emerald-700'
}

function savePriorityLead(lead) {
  toast.success(`${lead.nama_bisnis} disiapkan untuk export manual.`)
}

function viewPriorityLead(lead) {
  toast.info(`Detail ${lead.nama_bisnis}: ${lead.status_website}, skor ${lead.skor_peluang}/10.`)
}

function contactIcon(lead) {
  const contact = `${lead.kontak_bisa_dihubungi || lead.kontak || ''} ${lead.email || ''} ${lead.instagram || ''}`.toLowerCase()
  if (contact.includes('@')) return MessageCircle
  if (contact.includes('instagram')) return Globe2
  return Phone
}

function formatStatus(status) {
  const labels = { draft: 'Draft', approved: 'Approved', skipped: 'Skipped', contacted: 'Contacted', closed: 'Closed' }
  return labels[status] || status || 'Draft'
}

function percentage(value, total) {
  if (!total) return '0%'
  return `${Math.round((Number(value || 0) / Number(total)) * 100)}%`
}

function openMaps(lead) {
  if (lead.google_maps_link) {
    window.open(lead.google_maps_link, '_blank', 'noopener,noreferrer')
    return
  }
  toast.info(`Link Maps untuk ${lead.nama_bisnis} belum tersedia.`)
}

function exportCsv() {
  const rows = filteredLeads.value
  if (!rows.length) {
    toast.info('Tidak ada lead untuk diekspor.')
    return
  }
  const header = ['nama_bisnis', 'kategori', 'kota', 'kontak', 'status_website', 'skor_peluang', 'status', 'google_maps_link']
  const csv = [
    header.join(','),
    ...rows.map((lead) =>
      header
        .map((key) => `"${String(lead[key] ?? '').replaceAll('"', '""')}"`)
        .join(',')
    ),
  ].join('\n')
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = 'petaklien-leads.csv'
  link.click()
  URL.revokeObjectURL(url)
  toast.success('CSV berhasil dibuat.')
}

function exportPdf() {
  const rows = filteredLeads.value
  if (!rows.length) {
    toast.info('Tidak ada lead untuk diekspor.')
    return
  }

  const doc = new jsPDF({ orientation: 'landscape', unit: 'pt', format: 'a4' })
  doc.setFont('helvetica', 'bold')
  doc.setFontSize(18)
  doc.text('PetaKlien Leads Export', 40, 40)
  doc.setFont('helvetica', 'normal')
  doc.setFontSize(10)
  doc.text(`Kota: ${form.city} | Kategori: ${form.category} | Radius: ${form.radius} km`, 40, 58)

  autoTable(doc, {
    startY: 76,
    head: [['Nama Bisnis', 'Kategori', 'Kota', 'Kontak', 'Status Web', 'Skor', 'Status']],
    body: rows.map((lead) => [
      lead.nama_bisnis || '-',
      lead.kategori || '-',
      lead.kota || '-',
      lead.kontak_bisa_dihubungi || lead.kontak || '-',
      lead.status_website || '-',
      String(lead.skor_peluang || '-'),
      formatStatus(lead.status),
    ]),
    styles: { fontSize: 9, cellPadding: 6 },
    headStyles: { fillColor: [88, 0, 216] },
  })

  doc.save('petaklien-leads.pdf')
  toast.success('PDF berhasil dibuat.')
}
</script>

<script>
export default {
  components: {
    MetricCard: {
      props: ['label', 'value', 'helper', 'helperClass', 'featured'],
      template: `
        <article class="rounded-xl border p-5 shadow-sm" :class="featured ? 'border-primary/20 bg-primary/5' : 'border-outline-variant bg-white'">
          <span class="text-xs font-black uppercase tracking-wide" :class="featured ? 'text-primary' : 'text-on-surface-variant'">{{ label }}</span>
          <div class="mt-2 flex items-end gap-2">
            <span class="text-3xl font-black" :class="featured ? 'text-primary' : 'text-on-surface'">{{ value }}</span>
            <span class="mb-1 text-xs font-black" :class="featured ? 'text-primary' : helperClass">{{ helper }}</span>
          </div>
        </article>
      `,
    },
    PriorityLead: {
      props: ['lead', 'eyeIcon'],
      emits: ['save', 'view'],
      computed: {
        cardClass() {
          return this.lead.highlighted ? 'bg-surface border-primary/40' : 'bg-white border-outline-variant'
        },
        tags() {
          const tags = []
          if (this.lead.status_website === 'Belum ada') tags.push('NO WEB')
          if (this.lead.status_website === 'Hanya sosial media') tags.push('HANYA SOSMED')
          if (String(this.lead.catatan || '').toLowerCase().includes('aktif')) tags.push('AKTIF')
          if (!tags.length) tags.push(this.lead.status_website || 'LEAD')
          return tags
        },
      },
      methods: {
        tagClass(tag) {
          if (tag.includes('NO WEB')) return 'bg-red-100 text-red-700'
          if (tag.includes('AKTIF')) return 'bg-emerald-100 text-emerald-700'
          if (tag.includes('SOSMED')) return 'bg-orange-100 text-orange-700'
          return 'bg-slate-100 text-slate-500'
        },
      },
      template: `
        <article class="cursor-pointer rounded-xl border p-4 transition hover:border-primary" :class="cardClass">
          <div class="mb-2 flex items-start justify-between gap-4">
            <div>
              <h3 class="font-black text-on-surface">{{ lead.nama_bisnis }}</h3>
              <p class="text-[10px] font-black uppercase tracking-wide text-on-surface-variant">{{ lead.kota }} • {{ lead.kategori }}</p>
            </div>
            <span class="text-lg font-black text-primary">{{ lead.skor_peluang }}</span>
          </div>
          <div class="mb-3 flex flex-wrap gap-2">
            <span v-for="tag in tags" :key="tag" class="rounded px-1.5 py-0.5 text-[9px] font-black" :class="tagClass(tag)">{{ tag }}</span>
          </div>
          <div class="flex gap-2">
            <button class="flex-1 rounded-lg bg-primary py-2 text-[10px] font-black text-white transition hover:bg-primary-strong" @click="$emit('save', lead)">Simpan ke Spreadsheet</button>
            <button class="rounded-lg border border-outline-variant p-2 transition hover:bg-surface-container" @click="$emit('view', lead)" aria-label="Lihat detail">
              <component :is="eyeIcon" class="h-4 w-4" />
            </button>
          </div>
        </article>
      `,
    },
  },
}
</script>
