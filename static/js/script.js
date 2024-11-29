$(document).ready(function () {
  // NAVBAR
  $(window).on("scroll", function () {
    const navbar = $("header");
    // jika scroll lebih dari 5 pixel
    if ($(this).scrollTop() > 5) {
      navbar.css("opacity", "0.9"); // ubah opacity
    } else {
      navbar.css("opacity", "1"); // kembalikan opacity
    }
  });

  // FORM
  $(".needs-validation").on("submit", function (event) {
    // cek validasi apakah semua input dalam form valid sesuai aturan HTML
    if (!this.checkValidity()) {
      // mencegah tindakan default dari event listener submit
      event.preventDefault();
    }
    // class dari bootstrap untuk menampilkan elemen validasi
    $(this).addClass("was-validated");
  });

  // SCROLL TO TOP
  // menampilkan tombol ketika scroll ke bawah
  $(window).scroll(function () {
    if ($(this).scrollTop() > 250) {
      $("#scrollToTop").removeClass("d-none"); // tampilkan tombol
    } else {
      $("#scrollToTop").addClass("d-none"); // sembunyikan tombol
    }
  });

  // scroll ke atas saat tombol diklik
  $("#scrollToTop").click(function () {
    $("html, body").scrollTop(0); // scroll ke atas
    return false; // mencegah form dikirim secara default
  });

  // FAQ
  // ambil semua pertanyaan dengan class faq-item
  $(".faq-item").each(function () {
    const $q = $(this); // simpan referensi
    const $answer = $q.find(".faq-answer");
    const $icon = $q.find(".faq-question i");

    // event listener ketika faq-item diklik
    $q.on("click", function () {
      // cek apakah display === none
      if ($answer.css("display") === "none") {
        $answer.slideDown(); // tampilkan jawaban + transisi
        $icon.removeClass("bi-plus").addClass("bi-dash"); // ganti ikon
      } else {
        $answer.slideUp(); // sembunyikan jawaban + transisi
        $icon.removeClass("bi-dash").addClass("bi-plus");
      }
    });
  });

  // FORM ERROR
  if ($("#formErrors").data("errors") === true) {
    var myModal = new bootstrap.Modal(document.getElementById("exampleModal"));
    myModal.show();
  }

  // PROFILE
  // ambil gambar awal preview
  let initialImageSrc = $("#profile-photo-preview").attr("src");

  // Preview Foto saat dipilih
  $("#profile-photo-input").on("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        $("#profile-photo-preview").attr("src", e.target.result); // Update preview image
      };
      reader.readAsDataURL(file);
    }
  });

  // Clear Button
  $("#clearBtn").on("click", function () {
    // Reset form terdekat dari tombol yang diklik
    $(this).closest("form")[0].reset();

    // Reset preview gambar
    $("#profile-photo-preview").attr("src", initialImageSrc);
  });

  // SLIDER
  let currentIndex = 0;
  const cardWidth = $(".slider-row .col-12").outerWidth(true);
  const totalCards = $(".slider-row .col-12").length;
  const maxIndex = totalCards - 3; // Jumlah card yang dapat terlihat sekaligus (ubah sesuai kebutuhan)

  // Fungsi untuk geser ke kanan
  function slideNext() {
    if (currentIndex < maxIndex) {
      currentIndex++;
    } else {
      currentIndex = 0; // Reset ke awal jika sudah mencapai akhir
    }
    $(".slider-row").css(
      "transform",
      `translateX(-${currentIndex * cardWidth}px)`
    );
  }

  // Fungsi untuk geser ke kiri
  function slidePrev() {
    if (currentIndex > 0) {
      currentIndex--;
    } else {
      currentIndex = maxIndex; // Reset ke akhir jika sudah di awal
    }
    $(".slider-row").css(
      "transform",
      `translateX(-${currentIndex * cardWidth}px)`
    );
  }

  // Event tombol next
  $("#next-btn").click(slideNext);

  // Event tombol previous
  $("#prev-btn").click(slidePrev);

  // CHANGE EMAIL
  $(".add-email").on("click", function () {
    $(".change-email-form").toggleClass("d-none d-block");
  });
});
