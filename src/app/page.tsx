import Link from "next/link";
import Image from "next/image";
import FadeIn from "@/components/FadeIn";

export default function Home() {
  return (
    <div className="min-h-screen bg-paper text-dark pt-16 lg:pt-20">
      {/* Hero Section (Editorial Grid) */}
      <section className="grid grid-cols-1 lg:grid-cols-12 min-h-[85vh] border-b border-dark">
        {/* Left Typography Area */}
        <div className="lg:col-span-7 flex flex-col justify-center p-10 lg:p-16 border-b lg:border-b-0 lg:border-r border-dark">
          <FadeIn>
            <h1 className="font-editorial text-6xl lg:text-8xl xl:text-9xl leading-[0.9] tracking-tight text-dark mb-8">
              Detail <br/> 
              <span className="italic text-namata-pink">Presisi.</span> <br/>
              Estetika.
            </h1>
          </FadeIn>
          
          <FadeIn delay={0.2}>
            <p className="text-xs lg:text-sm max-w-sm uppercase tracking-widest leading-relaxed mb-12">
              Nail art dan eyelash treatment dengan standar studio profesional. Tidak ada kompromi pada kualitas.
            </p>
          </FadeIn>
          
          <FadeIn delay={0.4}>
            <div>
              <Link href="/booking" className="inline-block border border-dark px-10 py-4 uppercase tracking-[0.2em] text-[10px] font-semibold hover:bg-dark hover:text-paper transition-colors">
                Reservasi Sekarang
              </Link>
            </div>
          </FadeIn>
        </div>
        
        {/* Right Image Area */}
        <div className="lg:col-span-5 relative bg-namata-pink min-h-[40vh] overflow-hidden group">
          <Image 
            src="https://images.unsplash.com/photo-1604654894610-df63bc536371?auto=format&fit=crop&w=800&q=80" 
            alt="Nail Art Close Up" 
            fill
            className="object-cover grayscale mix-blend-multiply opacity-80 group-hover:scale-105 transition-transform duration-1000" 
            priority
          />
          <div className="absolute bottom-4 right-4 bg-paper px-4 py-2 uppercase tracking-[0.2em] text-[9px] font-bold border border-dark text-dark">
            Signature Art
          </div>
        </div>
      </section>

      {/* Services / Treatments (Flat Cards) */}
      <section id="treatments" className="grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-dark border-b border-dark">
        
        <div className="p-10 hover:bg-namata-pink transition-colors cursor-pointer group">
          <FadeIn>
            <div className="font-editorial text-4xl mb-4 italic">01.</div>
            <h3 className="uppercase tracking-[0.15em] text-xs font-bold mb-4">Nail Art</h3>
            <p className="text-sm font-light leading-relaxed mb-8 opacity-80">Dari desain minimalis hingga intricate hand-drawing. Menggunakan gel berkualitas premium yang tahan lama.</p>
            <div className="w-full border-t border-dark pt-4 flex justify-between uppercase tracking-widest text-[9px]">
              <span>Start from</span>
              <span className="font-bold">Rp 75k</span>
            </div>
          </FadeIn>
        </div>

        <div className="p-10 hover:bg-namata-pink transition-colors cursor-pointer group">
          <FadeIn delay={0.2}>
            <div className="font-editorial text-4xl mb-4 italic">02.</div>
            <h3 className="uppercase tracking-[0.15em] text-xs font-bold mb-4">Eyelash Ext.</h3>
            <p className="text-sm font-light leading-relaxed mb-8 opacity-80">Teknik pemasangan helai demi helai yang aman, ringan, dan tidak merusak bulu mata asli.</p>
            <div className="w-full border-t border-dark pt-4 flex justify-between uppercase tracking-widest text-[9px]">
              <span>Start from</span>
              <span className="font-bold">Rp 120k</span>
            </div>
          </FadeIn>
        </div>

        <Link href="/booking" className="block p-10 hover:bg-namata-pink transition-colors cursor-pointer group bg-dark text-paper">
          <FadeIn delay={0.4}>
            <div className="font-editorial text-4xl mb-4 italic text-namata-pink">03.</div>
            <h3 className="uppercase tracking-[0.15em] text-xs font-bold mb-4">Booking</h3>
            <p className="text-sm font-light leading-relaxed mb-8 opacity-80">Jadwalkan kedatanganmu sekarang. Kami menerapkan sistem reservasi untuk memastikan setiap klien mendapat pelayanan maksimal.</p>
            <div className="w-full border-t border-paper/30 pt-4 flex justify-between uppercase tracking-widest text-[9px]">
              <span>Status</span>
              <span className="font-bold text-namata-pink">Available</span>
            </div>
          </FadeIn>
        </Link>

      </section>

      {/* Artists Section */}
      <section id="artists" className="py-20 lg:py-32 px-6 border-b border-dark">
        <div className="max-w-7xl mx-auto">
          <FadeIn>
            <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
              <h2 className="font-editorial text-5xl lg:text-7xl font-bold text-dark leading-none">
                Meet Our <br/>
                <span className="italic text-namata-pink">Artists.</span>
              </h2>
              <p className="text-xs max-w-xs uppercase tracking-widest leading-relaxed">
                Tim profesional kami siap mewujudkan referensi desain terbaikmu.
              </p>
            </div>
          </FadeIn>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-8">
            {[
              { id: 'N1', name: "NISA", role: "NAIL TECHNICIAN", image: "https://images.unsplash.com/photo-1522337660859-02fbefca4702?auto=format&fit=crop&w=600&q=80" },
              { id: 'N2', name: "AMEL", role: "LASH ARTIST", image: "https://images.unsplash.com/photo-1516975080661-46b0a1f062bd?auto=format&fit=crop&w=600&q=80" },
              { id: 'N3', name: "DINA", role: "NAIL TECHNICIAN", image: "https://images.unsplash.com/photo-1616847259166-5121b66dfa04?auto=format&fit=crop&w=600&q=80" },
            ].map((artist, idx) => (
              <FadeIn key={artist.name} delay={idx * 0.1}>
                <Link href={`/booking?artist=${artist.id}`} className="group cursor-pointer block border border-dark p-2 hover:bg-dark hover:text-paper transition-colors duration-500">
                  <div className="relative aspect-[3/4] overflow-hidden bg-namata-pink/20 mb-4 border border-dark">
                    <Image src={artist.image} alt={artist.name} fill className="object-cover grayscale group-hover:grayscale-0 transition-all duration-700" />
                  </div>
                  <div className="px-2 pb-2">
                    <h3 className="font-editorial text-2xl font-bold mb-1">{artist.name}</h3>
                    <div className="w-full border-t border-dark/20 group-hover:border-paper/20 pt-2 flex justify-between uppercase tracking-widest text-[8px]">
                      <span>{artist.role}</span>
                      <span>→</span>
                    </div>
                  </div>
                </Link>
              </FadeIn>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
